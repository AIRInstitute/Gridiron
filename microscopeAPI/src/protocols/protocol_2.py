from time import sleep
from opentrons import simulate,execute,types
import json
import datetime
from opentrons import protocol_api
import urllib.request
from urllib import parse


metadata = {
    'protocolName': 'My Protocol',
    'author': 'Name <email@address.com>',
    'description': 'Simple protocol to get started using OT2',
    'apiLevel': '2.12'
}

#-------------------------------------------------------------------------------------------------------------------------
# Functions
#-------------------------------------------------------------------------------------------------------------------------
def create_history (nLetters,number):
    history = []
    #For A to Letter
    for i in range(0,nLetters):
        #For 1 to number
        for j in range(0,number):
            #Add the string to the list
            history.append(str(chr(65+i))+str(j+1))
    return history

def back_home(pipette1000):
    if (pipette1000.has_tip):
        pipette1000.drop_tip()
    protocol.home() 
    pipette1000.home_plunger()
    pipette1000.home() 
    
#############################################
#             START PROTOCOL                #
#############################################

# protocol = execute.get_protocol_api('2.12')
protocol = simulate.get_protocol_api('2.12')

def run(protocol: protocol_api.ProtocolContext):

    #------------------------------------------
    # Get data test
    #------------------------------------------
    url = "http://reqres.in/api/products%22"
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent,} 

    request=urllib.request.Request(url,None,headers)
    response = urllib.request.urlopen(request)
    data = response.read() 
    json_data = json.loads(data)

    volume = json_data["page"]

    #---------------------------------------------------------------------------------------------------------------------------
    # Protocol 2 implementation
    #---------------------------------------------------------------------------------------------------------------------------

    #----------------------------------------
    # Labware setup
    #----------------------------------------

    #--------------------------------------------
    #TODO Orion call getting parametres for liquid handler
    #-------------------------------------------- 

    n_eppendorfs = 24
    volume_falcons = [9600]
    current_falcon_volume = volume_falcons[0]
    V_EPPENDORF = 400


    #Mount pipette
    pipette1000 = protocol.load_instrument('p1000_single_gen2', 'right')

    tiprack1000 = protocol.load_labware('opentrons_96_tiprack_1000ul', 3)
    tiprack1000_history = create_history(8,12)

    # Mount falcon tube rack
    falcon = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 1)
    falcon_history = ["B4"]

    # Mount Eppendorf tube rack
    eppendorf = protocol.load_labware('opentrons_24_tuberack_eppendorf_2ml_safelock_snapcap', 4)
    eppendorf_history = create_history(4,6)

    #----------------------------------------
    # Protocol implementation
    #----------------------------------------
    timeStart = datetime.datetime.now()

    if(n_eppendorfs*V_EPPENDORF>volume_falcons[0]):
        protocol.comment("No enough volume in falcon to supply al the eppendorfs.")
        back_home(pipette1000)

    else:
        pipette1000.pick_up_tip(tiprack1000[tiprack1000_history[0]])
        tiprack1000_history.pop(0)
        for e in range(n_eppendorfs):
            if(current_falcon_volume<V_EPPENDORF):
                if(len(volume_falcons)!=1):
                    volume_falcons.pop(0)
                    current_falcon_volume = volume_falcons[0]
                    falcon_history.pop(0)
                    protocol.comment("Falcon tube empty. New falcon tube in use: "+falcon_history[0])
                else:
                    protocol.comment("No more falcon tubes available. Exiting")
                    back_home(pipette1000)
                    break

            for i in range(3):
                timeFirstTransfeStart = datetime.datetime.now()
                pipette1000.aspirate(100, falcon[falcon_history[0]], rate=2.0)
                pipette1000.dispense(100, falcon[falcon_history[0]], rate=2.0)
            
            pipette1000.aspirate(V_EPPENDORF, falcon[falcon_history[0]], rate=2.0)
            pipette1000.dispense(V_EPPENDORF, eppendorf[eppendorf_history[0]], rate=2.0)

            current_falcon_volume-=V_EPPENDORF

            for i in range(3):
                pipette1000.aspirate(100, eppendorf[eppendorf_history[0]], rate=2.0)
                pipette1000.dispense(100, eppendorf[eppendorf_history[0]].top, rate=2.0)
            
            # pipette1000.drop_tip()

            eppendorf_history.pop(0)
            timeFirstTransferEnd = datetime.datetime.now()


        #---------------------------------------------------------------------------------------------------------------------

        timeEnd = datetime.datetime.now()
        protocol.comment("Protocol 2 finished. Remove the eppendorf tubes")
        back_home(pipette1000)

        print("timeStart: " + str(timeStart))
        protocol.comment("timeStart: " + str(timeStart))

        print("timeEnd: " + str(timeEnd))
        protocol.comment("timeEnd: " + str(timeEnd))

        #------------------------------------------
        # Create datamodel
        #------------------------------------------

        data = {
            'timeStart': {
                "type": "datetime",
                "value": timeStart.isoformat()
            },
            'timeFirstTransfeStart': {
                "type": "datetime",
                "value":timeFirstTransfeStart.isoformat()
            },
            'timeFirstTransferEnd': {
                "type": "datetime",
                "value": timeFirstTransferEnd.isoformat()
            },
            'intervalSetup':{
                "type": "Float",
                "value": (timeFirstTransfeStart - timeStart).total_seconds()
            },
            'intervalFirstTransfer':{
                "type": "Float",
                "value":(timeFirstTransferEnd - timeFirstTransfeStart).total_seconds()
            },
            'intervalTransfer':{
                "type": "Float",
                "value": (timeEnd - timeFirstTransferEnd).total_seconds()
            },
            'intervalProcess':{
                "type": "Float",
                "value": (timeEnd - timeStart).total_seconds()
            },
            'protocol':{
                "type":"Integer",
                "value":2
            }
        }



        #------------------------------------------
        # Create data file
        #------------------------------------------
        try:
            with open('json_data.json', 'w') as outfile:
                json.dump(data, outfile)        

        except Exception as e:
            print("Error creating data file ")
            print(e)
            protocol.comment("Error creating data file ")
            protocol.comment(e)