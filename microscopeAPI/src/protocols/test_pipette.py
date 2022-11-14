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


protocol = execute.get_protocol_api('2.12')
# protocol = simulate.get_protocol_api('2.12')

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
    protocol.comment("volume: " + str(volume))
    print("volume: " + str(volume))

    #---------------------------
    # Move test
    #--------------------------
    pipette = protocol.load_instrument('p300_single_gen2', 'left')
    plate = protocol.load_labware('corning_12_wellplate_6.9ml_flat', 1)

    timeStart = datetime.datetime.now()
    timeFirstTransfeStart = datetime.datetime.now()
    pipette.move_to(plate['B2'].center().move(types.Point(z=100)))
    # sleep(1)
    pipette.home()  # Homes the axis and plunger
    protocol.home()
    timeFirstTransferEnd = datetime.datetime.now()


    timeEnd = datetime.datetime.now()

    print("timeStart: " + str(timeStart))
    protocol.comment("timeStart: " + str(timeStart))

    print("timeEnd: " + str(timeEnd))
    protocol.comment("timeEnd: " + str(timeEnd))

    #------------------------------------------
    # Create datamodel
    #------------------------------------------
    data = {
            'id':"urn:ngsi-ld:protocol-readings-001",
            'type':"PipettingProcess",
            'timeStart': {
                "type": "datetime",
                "value": timeStart.isoformat(),
                "metadata":"Time when the protocol started"
            },
            'timeFirstTransfeStart': {
                "type": "datetime",
                "value":timeFirstTransfeStart.isoformat(),
                "metadata":"Time when the first transfer started"
            },
            'timeFirstTransferEnd': {
                "type": "datetime",
                "value": timeFirstTransferEnd.isoformat(),
                "metadata":"Time when the first transfer ended"
            },
            'intervalSetup':{
                "type": "Float",
                "value": (timeFirstTransfeStart - timeStart).total_seconds(),
                "metadata":"Time it took to setup the labware in seconds"
            },
            'intervalFirstTransfer':{
                "type": "Float",
                "value":(timeFirstTransferEnd - timeFirstTransfeStart).total_seconds(),
                "metadata":"Time it took to do the first transfer in seconds"
            },
            'intervalTransfer':{
                "type": "Float",
                "value": (timeEnd - timeFirstTransferEnd).total_seconds(),
                "metadata":"Time it took to do the pipetting transfer in seconds"
            },
            'intervalProcess':{
                "type": "Float",
                "value": (timeEnd - timeStart).total_seconds(),
                "metadata":"Time it took to do the pipetting process in seconds"
            },
            'protocol':{
                "type":"Integer",
                "value":4,
                "metadata":"Which protocol was executed"
            }
        }
        
    #------------------------------------------
    # Send data
    #------------------------------------------
    # url = "http://212.128.140.209:1026/v2/entities"
    # url ="http://192.168.2.233:8080/test"
    # data = json.dumps(data)
    # data = data.encode()

    try:
        # req = urllib.request.Request(url, method="POST")
        # req.add_header('Content-Type', 'application/json')
        
        # r = urllib.request.urlopen(req, data=data)
        # content = r.read()
        # print(content)
        

        # import subprocess
        # command = "curl -d " +data+" -H 'Content-Type: application/json' -X POST http://192.168.2.233:8080/test"
        # p = subprocess.run(command, shell=True) 


        # Write file directly
        with open('json_data.json', 'w') as outfile:
            json.dump(data, outfile)        

    except Exception as e:
        print("##################################### Error: ")
        print(e)
        protocol.comment("###################################### Error: ")
        protocol.comment(e)


    # If error sending, trying with subrprocess
    #------------------
    # import subprocess
    # command = "curl -X POST'"+url+"'-H 'Content-Type: application/json' -d '"+data+"'"
    # p = subprocess.run(command, shell=True) 

        