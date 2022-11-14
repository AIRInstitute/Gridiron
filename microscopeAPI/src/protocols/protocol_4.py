from time import sleep
from opentrons import simulate,execute,types
import json
import datetime
from opentrons import protocol_api
import urllib.request
from urllib import parse
import json


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
    if(pipette1000.has_tip):
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
    # Protocol 4 implementation
    #---------------------------------------------------------------------------------------------------------------------------

    #----------------------------------------
    # Labware setup
    #----------------------------------------

    #--------------------------------------------
    #TODO Orion call getting parametres for liquid handler
    #-------------------------------------------- 
    
    n_eppendorfs = 24
  
    #Mount pipette
    pipette1000 = protocol.load_instrument('p1000_single_gen2', 'right')

    tiprack1000 = protocol.load_labware('opentrons_96_tiprack_1000ul', 3)
    tiprack1000_history = create_history(8,12)

    # Mount Eppendorf tube rack
    eppendorf = protocol.load_labware('opentrons_24_tuberack_eppendorf_2ml_safelock_snapcap', 4)
    eppendorf_history = create_history(4,6)

    # Mout cuvette
    with open("./labware/embio_kuberack_12.5.json") as f:
        cuvette_dict = json.load(f)
    cuvette_history = create_history(5,8)
    cuvette = protocol.load_labware_from_definition(cuvette_dict,9)

    #----------------------------------------
    # Protocol implementation
    #----------------------------------------
    timeStart = datetime.datetime.now()

    for e in range(n_eppendorfs):
        pipette1000.pick_up_tip(tiprack1000[tiprack1000_history[0]])
        tiprack1000_history.pop(0)

        for i in range(3):
            timeFirstTransfeStart = datetime.datetime.now()
            pipette1000.aspirate(100, eppendorf[eppendorf_history[0]], rate=2.0)
            pipette1000.dispense(100, eppendorf[eppendorf_history[0]], rate=2.0)
        
        pipette1000.aspirate(400, eppendorf[eppendorf_history[0]], rate=2.0)
        pipette1000.dispense(400, cuvette[cuvette_history[0]].bottom(22), rate=2.0)

        pipette1000.drop_tip()
        cuvette_history.pop(0)
        eppendorf_history.pop(0)
        timeFirstTransferEnd = datetime.datetime.now()
       

    #--------------------------------------------------------------------------------------------------------------------------------------    
    timeEnd = datetime.datetime.now()
    protocol.comment("Protocol 4 finished. Remove the cuvettes")
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
                "value":4
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