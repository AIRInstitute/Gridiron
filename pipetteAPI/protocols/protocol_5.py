N_WELL_RACKS = 4
N_CUVETTES = 24
URL = "test"





from time import sleep
from opentrons import simulate,execute,types
import json
import datetime
from opentrons import protocol_api
import urllib.request
from urllib import parse
import os


metadata = {
    'protocolName': 'My Protocol',
    'author': 'Name <email@address.com>',
    'description': 'Simple protocol to get started using OT2',
    'apiLevel': '2.12'
}

#-------------------------------------------------------------------------------------------------------------------------
# Functions
#-------------------------------------------------------------------------------------------------------------------------
def create_history (nLetters,Float):
    history = []
    #For A to Letter
    for i in range(0,nLetters):
        #For 1 to Float
        for j in range(0,Float):
            #Add the string to the list
            history.append(str(chr(65+i))+str(j+1))
    return history

def back_home(pipette300):
    if (pipette300.has_tip):
        pipette300.drop_tip()
    protocol.home() 
    pipette300.home_plunger()
    pipette300.home() 
    
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


    #---------------------------------------------------------------------------------------------------------------------------
    # Protocol 5 implementation
    #---------------------------------------------------------------------------------------------------------------------------
    timeStart = datetime.datetime.now()

    #----------------------------------------
    # Labware setup
    #----------------------------------------
    
    #--------------------------------------------
    #TODO Orion call getting parametres for liquid handler
    #-------------------------------------------- 

    n_cuvettes = N_CUVETTES
    n_well_racks = N_WELL_RACKS
  
    #Mount pipette
    pipette300 = protocol.load_instrument('p300_single_gen2', 'left')

    tiprack300 = protocol.load_labware('opentrons_96_tiprack_300ul', 2)
    tiprack300_history = create_history(8,12)

      # Mout cuvette
    with open("./labware/embio_kuberack_12.5.json") as f:
        cuvette_dict = json.load(f)
    cuvette_history = create_history(5,8)
    cuvette = protocol.load_labware_from_definition(cuvette_dict,9)

    # Mount well plates
    wellPlates = []

    if(n_well_racks>4):
        protocol.comment("Can't support so many well racks. Exiting")
        print("Can't support so many well racks. Exiting")
        back_home(pipette300)

    elif(n_well_racks*6<n_cuvettes):
        protocol.comment("Not enough welplates racks for the sameples specified. Exiting")
        print("Not enough welplates racks for the sameples specified. Exiting")
        back_home(pipette300)

    else:
        for i in range(n_well_racks):
            wellPlates.append(protocol.load_labware('corning_6_wellplate_16.8ml_flat', 5+i))

        #----------------------------------------
        # Protocol implementation
        #----------------------------------------
        timeStart = datetime.datetime.now()

        wellPlate = wellPlates[0]
        wellPlate_history = create_history(2,3)
        cont = 0
        for e in range(n_cuvettes):
            
            if(cont==6):
                cont = 0
                wellPlates.pop(0)
                wellPlate = wellPlates[0]
                wellPlate_history = create_history(2,3)
                protocol.comment("Changing wellplate rack")

            pipette300.pick_up_tip(tiprack300[tiprack300_history[0]])
            tiprack300_history.pop(0)

            for j in range(3):
                timeFirstTransfeStart = datetime.datetime.now()
                pipette300.aspirate(100, cuvette[cuvette_history[0]], rate=2.0)
                pipette300.dispense(100, cuvette[cuvette_history[0]], rate=2.0)
            
            for k in range(2):   # ASSUMING CUVETTES HAVE 200uL. 2 CUVETTES ASPIRATIONS PER CUVETTE 
                pipette300.aspirate(200, cuvette[cuvette_history[0]], rate=2.0)
                pipette300.dispense(200, wellPlate[wellPlate_history[0]], rate=2.0)

            wellPlate_history.pop(0)
            pipette300.drop_tip()
            cont += 1

            cuvette_history.pop(0)
            timeFirstTransferEnd = datetime.datetime.now()

        #--------------------------------------------------------------------------------------------------------------------------------------    
        timeEnd = datetime.datetime.now()
        protocol.comment("Protocol 5 finished. Remove the cuvettes")
        back_home(pipette300)

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
        # url = "http://212.128.140.209:7896/iot/json?k=4jggokgpepnvsb2uv4s40d59ov2&i=liquidHandler001"
        # url = "http://212.128.155.117:8081/test_agent"
        # url = "http://" + os.environ.get("ENDPOINT_AGENT") + ":" + os.environ.get("PORT_AGENT") + "/iot/json?k=" + os.environ.get("API_KEY") + "&i=" + os.environ.get("DEVICE_ID")
        url = URL

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

# N_WELL_RACKS = 4
# N_CUVETTES = 24
