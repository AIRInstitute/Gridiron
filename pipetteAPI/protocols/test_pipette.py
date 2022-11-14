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

    volume = VOLUME
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

VOLUME = 69