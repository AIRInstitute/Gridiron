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

def check_falcon_volume(current_volume,falcon_volume_needed):
    #Check if the volume is in the falcon history
    if (current_volume < falcon_volume_needed):
        return True
    else:
        return False

def back_home(pipette300,pipette1000):
    if (pipette1000.has_tip):
        pipette1000.drop_tip()
    if (pipette300.has_tip):
        pipette300.drop_tip()
    protocol.pause()
    protocol.home() 
    pipette300.home_plunger()
    pipette1000.home_plunger()
    pipette300.home() 
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
    # url = "http://reqres.in/api/products%22"
    # user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    # headers={'User-Agent':user_agent,} 

    # request=urllib.request.Request(url,None,headers)
    # response = urllib.request.urlopen(request)
    # data = response.read() 
    # json_data = json.loads(data)

    # volume = json_data["page"]

    #---------------------------------------------------------------------------------------------------------------------------
    # Protocol 1 implementation
    #---------------------------------------------------------------------------------------------------------------------------

    #----------------------------------------
    # Labware setup
    #----------------------------------------

    #--------------------------------------------
    #TODO Orion call getting parametres for liquid handler
    #-------------------------------------------- 

    n_eppendorfs = N_EPPENDORFS
    n_falcons = N_FALCONS_15ML
    volume_needed = VOLUME_NEEDED
    # STARTING_FALCON_VOLUME = 5000

    #Mount pipette
    pipette1000 = protocol.load_instrument('p1000_single_gen2', 'right')
    pipette300 = protocol.load_instrument('p300_single_gen2', 'left')

    #Mount falcon tube rack 
    falcon = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 1)
    falcon_history = ["A1","A2","B1","B2","C1","C2","A3","A4","B3","B4",]
    falcon_history = falcon_history[0:n_falcons]

    #Mount tiprack 
    tiprack300 = protocol.load_labware('opentrons_96_tiprack_300ul', 2)
    tiprack300_history = create_history(8,12) 

    tiprack1000 = protocol.load_labware('opentrons_96_tiprack_1000ul', 3)
    tiprack1000_history = create_history(8,12)

    # Mount Eppendorf tube rack
    eppendorf = protocol.load_labware('opentrons_24_tuberack_eppendorf_2ml_safelock_snapcap', 4)
    eppendorf_history = create_history(4,6)
    
    timeStart = datetime.datetime.now()

    #----------------------------------------
    # Protocol implementation
    #----------------------------------------
    
    if(len(volume_needed) != n_falcons):
        protocol.comment("The number of falcons is not equal to the number of volumes needed")
        protocol.comment("Exiting protocol")
        print("The number of falcons is not equal to the number of volumes needed")
        back_home(pipette300,pipette1000)
    
    else:
        pipette1000.pick_up_tip(tiprack1000[tiprack1000_history[0]])
        tiprack1000_history.pop(0)

        # Mix the falcon tube 
        for i in range(3):
            pipette1000.aspirate(1000, falcon[falcon_history[0]], rate=2.0)
            pipette1000.dispense(1000, falcon[falcon_history[0]], rate=2.0)  

        current_falcon_volume = STARTING_FALCON_VOLUME
        current_tip = 1000

        for e in range(n_eppendorfs):
            timeFirstTransfeStart = datetime.datetime.now()
            if check_falcon_volume(current_falcon_volume,volume_needed[0]):
                if(len(volume_needed)!=1):
                    falcon_history.pop(0)
                    volume_needed.pop(0)
                    protocol.comment("Falcon tube empty. New falcon tube in use: "+falcon_history[0])

                    current_falcon_volume = STARTING_FALCON_VOLUME
                    if(pipette1000.has_tip):
                        pipette1000.drop_tip()
                    pipette1000.pick_up_tip(tiprack1000[tiprack1000_history[0]])
                    tiprack1000_history.pop(0)

                    current_tip = 1000

                    # Mix the falcon tube 
                    for i in range(3):
                        pipette1000.aspirate(1000, falcon[falcon_history[0]], rate=2.0)
                        pipette1000.dispense(1000, falcon[falcon_history[0]], rate=2.0)  
                else:
                    protocol.comment("Falcon tube empty. No more falcon tubes available. Exiting")
                    back_home(pipette300,pipette1000)
                    break

            # Transfer to eppendorf tube taken into account the volume needed
            if volume_needed[0] <= 300:
                if(pipette1000.has_tip):
                    pipette1000.drop_tip()

                if(not pipette300.has_tip):
                    pipette300.pick_up_tip(tiprack300[tiprack300_history[0]])

                tiprack300_history.pop(0) 

                pipette300.aspirate(100, falcon[falcon_history[0]], rate=2.0)
                pipette300.dispense(100, falcon[falcon_history[0]], rate=2.0)

                pipette300.aspirate(volume_needed[0], falcon[falcon_history[0]], rate=2.0)
                pipette300.dispense(volume_needed[0], eppendorf[eppendorf_history[0]], rate=2.0)

                current_falcon_volume = current_falcon_volume - volume_needed[0]

                # pipette300.drop_tip()
                eppendorf_history.pop(0)
            
            else:
                # if current_tip == 0:
                #     pipette1000.pick_up_tip(tiprack1000[tiprack1000_history[0]]) 
                #     tiprack1000_history.pop(0) 
                    
                # current_tip = 0

                if(not pipette1000.has_tip):
                    pipette1000.pick_up_tip(tiprack1000[tiprack1000_history[0]])

                if(pipette300.has_tip):
                    pipette300.drop_tip()

                pipette1000.aspirate(100, falcon[falcon_history[0]], rate=2.0)
                pipette1000.dispense(100, falcon[falcon_history[0]], rate=2.0)

                pipette1000.aspirate(volume_needed[0], falcon[falcon_history[0]], rate=2.0)
                pipette1000.dispense(volume_needed[0], eppendorf[eppendorf_history[0]], rate=2.0)

                current_falcon_volume = current_falcon_volume - volume_needed[0]
                eppendorf_history.pop(0)
                # pipette1000.drop_tip()
            
            timeFirstTransferEnd = datetime.datetime.now()

        # ------------------------------------------------------------------------------------------------------------------------------------------------------------

        timeEnd = datetime.datetime.now()
        protocol.comment("Protocol 1 finished. Remove the eppendorf tubes")
        back_home(pipette300,pipette1000)

        print("timeStart: " + str(timeStart))
        protocol.comment("timeStart: " + str(timeStart))

        print("timeEnd: " + str(timeEnd))
        protocol.comment("timeEnd: " + str(timeEnd))

        #------------------------------------------
        # Create datamodel
        #------------------------------------------

        data = {
            'timeStart':timeStart.isoformat(),
            'timeFirstTransfeStart': timeFirstTransfeStart.isoformat(),  
            'timeFirstTransferEnd': timeFirstTransferEnd.isoformat(),
            'intervalSetup': (timeFirstTransfeStart - timeStart).total_seconds(),
            'intervalFirstTransfer':(timeFirstTransferEnd - timeFirstTransfeStart).total_seconds(),
            'intervalTransfer':(timeEnd - timeFirstTransferEnd).total_seconds(),
            'intervalProcess':(timeEnd - timeStart).total_seconds(),
            'protocol':4
        }
    
        payload = json.dumps(data)

        #------------------------------------------
        # Send data
        #------------------------------------------

        import requests 
        url = "http://212.128.140.209:7896/iot/json?k=4jggokgpepnvsb2uv4s40d59ov2&i=liquidHandler001"
        # url = "http://212.128.155.117:8081/test_agent"
        
        headers = {
            'Content-Type': 'application/json',
            'fiware-services': 'openiot'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        # print(response.text)

        #------------------------------------------
        # Create data file
        #------------------------------------------
        # try:
        #     with open('json_data.json', 'w') as outfile:
        #         json.dump(data, outfile)        

        # except Exception as e:
        #     print("Error creating data file ")
        #     print(e)
        #     protocol.comment("Error creating data file ")
        #     protocol.comment(e)

VOLUME_NEEDED = [500,400,300,250]
STARTING_FALCON_VOLUME = 5000
N_FALCONS_15ML = 4
N_EPPENDORFS = 24
