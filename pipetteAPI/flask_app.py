from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
import requests
import json
import random
import datetime
from PIL import Image
from numpy import asarray
import os

#------------------------------------------
# For ssh connection
#------------------------------------------
# NECESSARY PARAMIKO >=2.7 for OPENSSH key compatibilty
import paramiko
import subprocess

app = Flask(__name__)

#------------------------------------------
# Load config
#------------------------------------------
CONFIGURATION_FILE = "./config.json"
CORS(app, resources={r'/*': {'origins': '*'}})

with open(CONFIGURATION_FILE) as json_file:
    config = json.load(json_file)

HOST=config["flask_server"]["host"]
PORT=config["flask_server"]["port"]
DEBUG=config["flask_server"]["debug"]

KEY = config["pipette"]["key"]
USERNAME = config["pipette"]["username"]
PIPETTE_HOST = config["pipette"]["hostname"]
PIPETTE_PORT = config["pipette"]["port"]

ORION_HOST = config["orion"]["host"]
ORION_PORT = config["orion"]["port"]

############################################
# START PROTOCOL
############################################

@app.route('/start_protocol', methods=['POST'])
def start_protocol():
    specifications = request.get_json()
    protocol = "0"

    # if(specifications["protocol"] == "test_pipette"):
    if 'test_pipette' in specifications:
        protocol = "test_pipette.py"
        file = open("./protocols/test_pipette.py")
        data = file.readlines()
        # Get VOLUME
        data[-1] = "VOLUME = "+str(specifications["volume"])+"\n"
        file = open("./protocols/test_pipette.py", "w")
        file.writelines(data)
        file.close()

    # if(specifications["protocol"] == "protocol_1"):
    if 'protocol1' in specifications:
        print('llego aqui 1')
        protocol = "protocol_1.py"
        file = open("./protocols/protocol_1.py")
        data = file.readlines()
        print('llego aqui 2')

        # N_EPPENDORFS = 24
        # N_FALCONS_15ML = 4
        # STARTING_FALCON_VOLUME = 5000
        # VOLUME_NEEDED = [500,340,200,420]
        print(specifications)

        data[0] = "N_EPPENDORFS = "+ str(specifications["protocol1"]["n_eppendorfs"]['value']) +"\n"
        data[1] = "N_FALCONS_15ML = "+ str(specifications["protocol1"]["n_falcons_15ml"]['value']) +"\n"
        data[2] = "STARTING_FALCON_VOLUME = "+ str(specifications["protocol1"]["starting_v_falcon"]['value']) +"\n"
        data[3] = "VOLUME_NEEDED = "+ str(list(map(int,specifications["protocol1"]["volume_falcons"]['value']))) +"\n"
        print("http://" + os.environ.get("ENDPOINT_AGENT") + ":" + os.environ.get("PORT_AGENT") + "/iot/json?k=" + os.environ.get("API_KEY") + "&i=" + os.environ.get("DEVICE_ID"))
        data[4] = "URL = '"+str("http://" + os.environ.get("ENDPOINT_AGENT") + ":" + os.environ.get("PORT_AGENT") + "/iot/json?k=" + os.environ.get("API_KEY") + "&i=" + os.environ.get("DEVICE_ID"))+"'"
        
        file = open("./protocols/protocol_1.py", "w")
        file.writelines(data)
        file.close()

    # if(specifications["protocol"] == "protocol_2"):
    if 'protocol2' in specifications:
        protocol = "protocol_2.py"
        file = open("./protocols/protocol_2.py")
        data = file.readlines()

        # N_EPPENDORFS = 24
        # STARTING_V_FALCON_B4 = 5000

        data[0] = "N_EPPENDORFS = "+ str(specifications["protocol2"]["n_eppendorfs"]['value']) +"\n"
        data[1] = "STARTING_V_FALCON_B4 = "+ str(specifications["protocol2"]["starting_v_falcon_B4"]['value']) +"\n"
        data[3] = "URL = '" + str("http://" + os.environ.get("ENDPOINT_AGENT") + ":" + os.environ.get("PORT_AGENT") + "/iot/json?k=" + os.environ.get("API_KEY") + "&i=" + os.environ.get("DEVICE_ID"))+"'"

        file = open("./protocols/protocol_2.py", "w")
        file.writelines(data)
        file.close()
    
    # if(specifications["protocol"] == "protocol_3"):
    if 'protocol3' in specifications:
        protocol = "protocol_3.py"
        file = open("./protocols/protocol_3.py")
        data = file.readlines()

        # N_EPPENDORFS = 24
        # N_WELL_RACKS = 6
        # VOLUME_FALCONS = [25000,25000,25000]

        data[0] = "N_EPPENDORFS = "+ str(specifications["protocol3"]["n_eppendorfs"]['value']) +"\n"
        # data[-2] = "VOLUME_FALCONS = "+ str(specifications["protocol3"]["volume_falcons"]) +"\n"
        data[2] = "N_WELL_RACKS = "+ str(specifications["protocol3"]["n_well_racks"]['value']) +"\n"
        data[3] = "URL = '" + str("http://" + os.environ.get("ENDPOINT_AGENT") + ":" + os.environ.get("PORT_AGENT") + "/iot/json?k=" + os.environ.get("API_KEY") + "&i=" + os.environ.get("DEVICE_ID"))+"'"

        file = open("./protocols/protocol_3.py", "w")
        file.writelines(data)
        file.close()
    
    # if(specifications["protocol"] == "protocol_4"):
    if 'protocol4' in specifications:
        protocol = "protocol_4.py"
        file = open("./protocols/protocol_4.py")
        data = file.readlines()

        # N_EPPENDORFS = 24

        data[0] = "N_EPPENDORFS = "+ str(specifications["protocol4"]["n_cuvettes"]['value']) +"\n"
        data[1] = "URL = '" + str("http://" + os.environ.get("ENDPOINT_AGENT") + ":" + os.environ.get("PORT_AGENT") + "/iot/json?k=" + os.environ.get("API_KEY") + "&i=" + os.environ.get("DEVICE_ID"))+"'"

        file = open("./protocols/protocol_4.py", "w")
        file.writelines(data)
        file.close()

    # if(specifications["protocol"] == "protocol_5"):
    if 'protocol5' in specifications:
        protocol = "protocol_5.py"
        file = open("./protocols/protocol_5.py")
        data = file.readlines()

        # N_CUVETTES = 24

        data[0] = "N_CUVETTES = "+ str(specifications["protocol5"]["n_cuvettes"]['value']) +"\n"
        data[1] = "N_WELL_RACKS = "+ str(specifications["protocol5"]["n_well_racks"]['value']) +"\n"
        data[2] = "URL = '" + str("http://" + os.environ.get("ENDPOINT_AGENT") + ":" + os.environ.get("PORT_AGENT") + "/iot/json?k=" + os.environ.get("API_KEY") + "&i=" + os.environ.get("DEVICE_ID"))+"'"

        file = open("./protocols/protocol_5.py", "w")
        file.writelines(data)
        file.close()        
        
    #--------------------------------------------
    # SCP connection for copying protocol file into robot
    #-------------------------------------------- 
    print('llego aqui 3')
    print("scp -i "+KEY+" ./protocols/"+protocol+" "+USERNAME+"@"+PIPETTE_HOST+":/data/"+protocol)
    try:
        print('entro en try scp 1')
        result = subprocess.run("scp -i "+KEY+" ./protocols/"+protocol+" "+USERNAME+"@"+PIPETTE_HOST+":/data/"+protocol, shell=True)
        if(result.returncode==0):
            print("SCP connection successful")
        else:
            print("SCP connection error")
            return make_response(jsonify({"command": "Error copying protocol file"}, 500))
    except subprocess.CalledProcessError as e:
        print(e.output)
        return make_response(jsonify({"command": "Error copying protocol file"}, 500))
        
    #--------------------------------------------
    # SSH connection for executing protocol
    #--------------------------------------------
    try:
        print('llego aqui 4')
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(PIPETTE_HOST, port=PIPETTE_PORT, username=USERNAME, key_filename=KEY)
        print('llego aqui 5')

        stdin, stdout, stderr = ssh.exec_command("opentrons_execute /data/"+protocol,get_pty=True)        # Non blocking call
        exit_status = stdout.channel.recv_exit_status()          # Blocking call,needs to wait for completition
        
        # Copying result file to local and read it
        #! NOT NECESSARY IF REQUESTS POST FROM PROTOCOL SENDS THE INFO TO THE JSON AGENT
        if exit_status == 0:                                    
            print("Pipetting operation finished. Reading results")
            try: 
                result = subprocess.run("scp -i "+KEY+" "+USERNAME+"@"+PIPETTE_HOST+":/root/json_data.json ./json_data.json", shell=True)
                if(result.returncode==0):
                    with open('./json_data.json') as json_file:
                        data = json.load(json_file)
                    print("SCP connection successful")
                    print(data)
                    ssh.close()
                    return make_response(jsonify({"command": "Operation finished"}, 200))
                else:
                    print("SCP connection error. Could not copy results")
                    ssh.close()
                    return make_response(jsonify({"command": "SCP connection error. Could not copy results"}, 500))
            except subprocess.CalledProcessError as e:
                print(e.output)
                ssh.close()
                return make_response(jsonify({"command": "Error copying result file"}, 500))
        else:
            print("Error", exit_status)
            ssh.close()
            return make_response(jsonify({"command": "Error executing protocol"}, 500))
        ssh.close()
    except Exception as e:
        print(e)
        ssh.close()
        return make_response(jsonify({"command" "Error executing protocol"}, 500))

    return make_response(jsonify({}, 200))

#------------------------------------------
# Test route
#------------------------------------------

@app.route('/test_write', methods=['GET', 'POST'])
def test_write():
    specifications = request.get_json()

    if(specifications["protocol"] == "test_pipette"):
        file = open("./protocols/test_pipette.py")
        data = file.readlines()
        # Get VOLUME
        data[-1] = "VOLUME = "+str(specifications["volume"])+"\n"
        file = open("./protocols/test_pipette.py", "w")
        file.writelines(data)
        file.close()

    if(specifications["protocol"] == "protocol_1"):
        file = open("./protocols/protocol_1.py")
        data = file.readlines()

        # N_EPPENDORFS = 24
        # N_FALCONS_15ML = 4
        # STARTING_FALCON_VOLUME = 5000
        # VOLUME_NEEDED = [500,340,200,420]

        data[-1] = "N_EPPENDORFS = "+ str(specifications["n_eppendorfs"]) +"\n"
        data[-2] = "N_FALCONS_15ML = "+ str(specifications["n_falcons_15ml"]) +"\n"
        data[-3] = "STARTING_FALCON_VOLUME = "+ str(specifications["starting_v_falcon_B4"]) +"\n"
        data[-4] = "VOLUME_NEEDED = "+ str(specifications["volume_falcons"]) +"\n"

        file = open("./protocols/protocol_1.py", "w")
        file.writelines(data)
        file.close()

    if(specifications["protocol"] == "protocol_2"):
        file = open("./protocols/protocol_2.py")
        data = file.readlines()

        # N_EPPENDORFS = 24
        # STARTING_V_FALCON_B4 = 5000

        data[-1] = "N_EPPENDORFS = "+ str(specifications["n_eppendorfs"]) +"\n"
        data[-2] = "STARTING_V_FALCON_B4 = "+ str(specifications["starting_v_falcon_B4"]) +"\n"

        file = open("./protocols/protocol_2.py", "w")
        file.writelines(data)
        file.close()
    
    if(specifications["protocol"] == "protocol_3"):
        file = open("./protocols/protocol_3.py")
        data = file.readlines()

        # N_EPPENDORFS = 24
        # N_WELL_RACKS = 6
        # VOLUME_FALCONS = [25000,25000,25000]

        data[-1] = "N_EPPENDORFS = "+ str(specifications["n_eppendorfs"]) +"\n"
        data[-2] = "VOLUME_FALCONS = "+ str(specifications["volume_falcons"]) +"\n"
        data[-3] = "N_WELL_RACKS = "+ str(specifications["n_well_racks"]) +"\n"

        file = open("./protocols/protocol_3.py", "w")
        file.writelines(data)
        file.close()
    
    if(specifications["protocol"] == "protocol_4"):
        file = open("./protocols/protocol_4.py")
        data = file.readlines()

        # N_EPPENDORFS = 24

        data[-1] = "N_EPPENDORFS = "+ str(specifications["n_eppendorfs"]) +"\n"

        file = open("./protocols/protocol_4.py", "w")
        file.writelines(data)
        file.close()

    if(specifications["protocol"] == "protocol_5"):
        file = open("./protocols/protocol_5.py")
        data = file.readlines()

        # N_CUVETTES = 24

        data[-1] = "N_CUVETTES = "+ str(specifications["n_cuvettes"]) +"\n"
        data[-2] = "N_WELL_RACKS = "+ str(specifications["n_well_racks"]) +"\n"

        file = open("./protocols/protocol_5.py", "w")
        file.writelines(data)
        file.close()
    
    return "OK"

@app.route('/test', methods=['GET'])
def test():
    # protocol_file = config["ot2_params"]["test"]
    try:
        result = subprocess.run("scp -i "+KEY+" ./protocols/test_pipette.py "+USERNAME+"@"+PIPETTE_HOST+":/data/test_pipette.py", shell=True)
        print(result)
        if(result.returncode==0):
            print("SCP connection successful")
        else:
            print("SCP connection error")
    except subprocess.CalledProcessError as e:
        print(e.output)
        print("Error")
        return "Error copying protocol file"
    
    #--------------------------------------------
    # SSH connection for executing protocol and retrieve results
    #--------------------------------------------
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(PIPETTE_HOST, port=PIPETTE_PORT, username=USERNAME, key_filename=KEY)

        stdin, stdout, stderr = ssh.exec_command("opentrons_execute /data/test_pipette.py",get_pty=True)        # Non blocking call
        exit_status = stdout.channel.recv_exit_status()          # Blocking call,needs to wait for completition
        # if exit_status == 0:                                    
        #     print("Pipetting operation finished. Reading results")
        #     try: 
        #         # Copying result file to local and read it
        #         result = subprocess.run("scp -i "+KEY+" "+USERNAME+"@"+PIPETTE_HOST+":/root/json_data.json ./json_data.json", shell=True)
        #         if(result.returncode==0):
        #             with open('./json_data.json') as json_file:
        #                 data = json.load(json_file)
        #                 print(data)

        #                 #--------------------------------------------
        #                 #TODO Orion call uploading data results
        #                 #-------------------------------------------- 

        #             print("SCP connection successful")
        #             return "Operation finished"
        #         else:
        #             print("SCP connection error. Could not copy results")
        #     except subprocess.CalledProcessError as e:
        #         print(e.output)
        #         return "Error copying protocol file"
        # else:
        #     print("Error", stderr)
        # ssh.close()
    except Exception as e:
        print(e)
        ssh.close()

    return "call done"

@app.route('/test_orion', methods=['GET'])
def test_orion():
    data={
        "volume_e": {
            "type": "Float",
            "value": random.randint(100, 500),
        },
        "n_falcons_15ml": {
            "type": "Integer",
            "value": random.randrange(4),
        },
        "volume_falcons": {
            "type": "Array",
            "value": [
                random.randint(100, 1000),
                random.randint(100, 1000),
                random.randint(100, 1000),
                random.randint(100, 1000)
            ],
        },
        "n_eppendorfs": {
            "type": "Integer",
            "value": random.randint(1, 24)
        },
        "starting_v_falcon": {
            "type": "Integer",
            "value": random.randint(2000, 5000)
        },
        "starting_v_falcon_B4": {
            "type": "Integer",
            "value": random.randint(5000, 9600)
        },
        "n_wellplates": {
            "type": "Integer",
            "value": random.randint(6,24)
        },
        "n_falcons_50ml": {
            "type": "Integer",
            "value": random.randint(6, 24)
        },
        "n_cuvettes": {
            "type": "Integer",
            "value": random.randint(6, 24)
        },
        "timeStart": {
            "type": "DateTime",
            "value": datetime.datetime.now().isoformat(),
        },
        "timeFirstTransfeStart": {
            "type": "DateTime",
            "value": datetime.datetime.now().isoformat()
        },
        "timeFirstTransferEnd": {
            "type": "DateTime",
            "value": datetime.datetime.now().isoformat()
        },
        "intervalSetup": {
            "type": "Float",
            "value": random.randint(10,30)
        },
        "intervalFirstTransfer": {
            "type": "Float",
            "value": random.randint(10,30)
        },
        "intervalTransfer": {
            "type": "Float",
            "value": random.randint(10,30)
        },
        "intervalProcess": {
            "type": "Float",
            "value": random.randint(10,30),
        },
        "protocol":{
            "type":"Integer",
            "value":0
        }
    }
    
    url_patch =  "http://"+str(ORION_HOST)+":"+str(ORION_PORT)+"/v2/entities/urn:ngsi-ld:protocol-readings-001/attrs"

    # print(data)
    data = json.dumps(data)
    headers = {'Content-Type':'application/json'}
    r = requests.patch(url_patch,data=data,headers=headers)
    print(r)
    if(r.status_code==204):
        # Only for data sending to orion
        return data
    else:
        return "Error "+ str(r.status_code)

@app.route('/test_agent', methods=['GET','POST'])
def test_agent():
    print("Llega")
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        return "OK"
#------------------------------------------
# Pipetting process
#------------------------------------------
@app.route('/start_protocol_1')
def pipetting_1():
    protocol_file = config["ot2_params"]["test"]
    # protocol_file = config["ot2_params"]["protocol_1"]
    
    #--------------------------------------------
    # SCP connection for copying protocol file into robot
    #-------------------------------------------- 
    try:
        result = subprocess.run("scp -i "+KEY+" ./protocols/"+protocol_file+" "+USERNAME+"@"+PIPETTE_HOST+":/data/"+protocol_file, shell=True)
        if(result.returncode==0):
            print("SCP connection successful")
        else:
            print("SCP connection error")
    except subprocess.CalledProcessError as e:
        print(e.output)
        return "Error copying protocol file"
        
    #--------------------------------------------
    # SSH connection for executing protocol and retrieve results
    #--------------------------------------------
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(PIPETTE_HOST, port=PIPETTE_PORT, username=USERNAME, key_filename=KEY)

        stdin, stdout, stderr = ssh.exec_command("opentrons_execute /data/"+protocol_file,get_pty=True)        # Non blocking call
        exit_status = stdout.channel.recv_exit_status()          # Blocking call,needs to wait for completition
        if exit_status == 0:                                    
            print("Pipetting operation finished. Reading results")
            try: 
                # Copying result file to local and read it
                result = subprocess.run("scp -i "+KEY+" "+USERNAME+"@"+PIPETTE_HOST+":/root/json_data.json ./json_data.json", shell=True)
                if(result.returncode==0):
                    with open('./json_data.json') as json_file:
                        data = json.load(json_file)
                      #  print(data)

                        #--------------------------------------------
                        #TODO Orion call uploading data results
                        #-------------------------------------------- 

                    print("SCP connection successful")
                    return "Operation finished"
                else:
                    print("SCP connection error. Could not copy results")
            except subprocess.CalledProcessError as e:
                print(e.output)
                return "Error copying protocol file"
        else:
            print("Error", exit_status)
        ssh.close()
    except Exception as e:
        print(e)
        ssh.close()

@app.route('/start_protocol_2')
def pipetting_2():
    protocol_file = config["ot2_params"]["test"]
    # protocol_file = config["ot2_params"]["protocol_2"]
    
    #--------------------------------------------
    #TODO Orion call uploading parametres for liquid handler
    #-------------------------------------------- 


    #--------------------------------------------
    # SCP connection for copying protocol file into robot
    #-------------------------------------------- 
    try:
        result = subprocess.run("scp -i "+KEY+" ./protocols/"+protocol_file+" "+USERNAME+"@"+PIPETTE_HOST+":/data/"+protocol_file, shell=True)
        if(result.returncode==0):
            print("SCP connection successful")
        else:
            print("SCP connection error")
    except subprocess.CalledProcessError as e:
        print(e.output)
        return "Error copying protocol file"
        
    #--------------------------------------------
    # SSH connection for executing protocol and retrieve results
    #--------------------------------------------
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(PIPETTE_HOST, port=PIPETTE_PORT, username=USERNAME, key_filename=KEY)

        stdin, stdout, stderr = ssh.exec_command("opentrons_execute /data/"+protocol_file,get_pty=True)        # Non blocking call
        exit_status = stdout.channel.recv_exit_status()          # Blocking call,needs to wait for completition
        if exit_status == 0:                                    
            print("Pipetting operation finished. Reading results")
            try: 
                # Copying result file to local and read it
                result = subprocess.run("scp -i "+KEY+" "+USERNAME+"@"+PIPETTE_HOST+":/root/json_data.json ./json_data.json", shell=True)
                if(result.returncode==0):
                    with open('./json_data.json') as json_file:
                        data = json.load(json_file)
                      #  print(data)
                        #--------------------------------------------
                        #TODO Orion call uploading data results
                        #-------------------------------------------- 

                    print("SCP connection successful")
                    return "Operation finished"
                else:
                    print("SCP connection error. Could not copy results")
            except subprocess.CalledProcessError as e:
                print(e.output)
                return "Error copying protocol file"
        else:
            print("Error", exit_status)
        ssh.close()
    except Exception as e:
        print(e)
        ssh.close()

@app.route('/start_protocol_3')
def pipetting_3():
    protocol_file = config["ot2_params"]["test"]
    # protocol_file = config["ot2_params"]["protocol_3"]
    
    #--------------------------------------------
    #TODO Orion call uploading parametres for liquid handler
    #-------------------------------------------- 


    #--------------------------------------------
    # SCP connection for copying protocol file into robot
    #-------------------------------------------- 
    try:
        result = subprocess.run("scp -i "+KEY+" ./protocols/"+protocol_file+" "+USERNAME+"@"+PIPETTE_HOST+":/data/"+protocol_file, shell=True)
        if(result.returncode==0):
            print("SCP connection successful")
        else:
            print("SCP connection error")
    except subprocess.CalledProcessError as e:
        print(e.output)
        return "Error copying protocol file"
        
    #--------------------------------------------
    # SSH connection for executing protocol and retrieve results
    #--------------------------------------------
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(PIPETTE_HOST, port=PIPETTE_PORT, username=USERNAME, key_filename=KEY)

        stdin, stdout, stderr = ssh.exec_command("opentrons_execute /data/"+protocol_file,get_pty=True)        # Non blocking call
        exit_status = stdout.channel.recv_exit_status()          # Blocking call,needs to wait for completition
        if exit_status == 0:                                    
            print("Pipetting operation finished. Reading results")
            try: 
                # Copying result file to local and read it
                result = subprocess.run("scp -i "+KEY+" "+USERNAME+"@"+PIPETTE_HOST+":/root/json_data.json ./json_data.json", shell=True)
                if(result.returncode==0):
                    with open('./json_data.json') as json_file:
                        data = json.load(json_file)
                      #  print(data)

                        #--------------------------------------------
                        #TODO Orion call uploading data results
                        #-------------------------------------------- 

                    print("SCP connection successful")
                    return "Operation finished"
                else:
                    print("SCP connection error. Could not copy results")
            except subprocess.CalledProcessError as e:
                print(e.output)
                return "Error copying protocol file"
        else:
            print("Error", exit_status)
        ssh.close()
    except Exception as e:
        print(e)
        ssh.close()

@app.route('/start_protocol_4')
def pipetting_4():
    protocol_file = config["ot2_params"]["test"]
    # protocol_file = config["ot2_params"]["protocol_4"]
    
    #--------------------------------------------
    #TODO Orion call uploading parametres for liquid handler
    #-------------------------------------------- 


    #--------------------------------------------
    # SCP connection for copying protocol file into robot
    #-------------------------------------------- 
    try:
        result = subprocess.run("scp -i "+KEY+" ./protocols/"+protocol_file+" "+USERNAME+"@"+PIPETTE_HOST+":/data/"+protocol_file, shell=True)
        if(result.returncode==0):
            print("SCP connection successful")
        else:
            print("SCP connection error")
    except subprocess.CalledProcessError as e:
        print(e.output)
        return "Error copying protocol file"
        
    #--------------------------------------------
    # SSH connection for executing protocol and retrieve results
    #--------------------------------------------
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(PIPETTE_HOST, port=PIPETTE_PORT, username=USERNAME, key_filename=KEY)

        stdin, stdout, stderr = ssh.exec_command("opentrons_execute /data/"+protocol_file,get_pty=True)        # Non blocking call
        exit_status = stdout.channel.recv_exit_status()          # Blocking call,needs to wait for completition
        if exit_status == 0:                                    
            print("Pipetting operation finished. Reading results")
            try: 
                # Copying result file to local and read it
                result = subprocess.run("scp -i "+KEY+" "+USERNAME+"@"+PIPETTE_HOST+":/root/json_data.json ./json_data.json", shell=True)
                if(result.returncode==0):
                    with open('./json_data.json') as json_file:
                        data = json.load(json_file)
                      #  print(data)

                        #--------------------------------------------
                        #TODO Orion call uploading data results
                        #-------------------------------------------- 

                    print("SCP connection successful")
                    return "Operation finished"
                else:
                    print("SCP connection error. Could not copy results")
            except subprocess.CalledProcessError as e:
                print(e.output)
                return "Error copying protocol file"
        else:
            print("Error", exit_status)
        ssh.close()
    except Exception as e:
        print(e)
        ssh.close()

@app.route('/start_protocol_5')
def pipetting_5():
    protocol_file = config["ot2_params"]["test"]
    # protocol_file = config["ot2_params"]["protocol_5"]
    
    #--------------------------------------------
    #TODO Orion call uploading parametres for liquid handler
    #-------------------------------------------- 


    #--------------------------------------------
    # SCP connection for copying protocol file into robot
    #-------------------------------------------- 
    try:
        result = subprocess.run("scp -i "+KEY+" ./protocols/"+protocol_file+" "+USERNAME+"@"+PIPETTE_HOST+":/data/"+protocol_file, shell=True)
        if(result.returncode==0):
            print("SCP connection successful")
        else:
            print("SCP connection error")
    except subprocess.CalledProcessError as e:
        print(e.output)
        return "Error copying protocol file"
        
    #--------------------------------------------
    # SSH connection for executing protocol and retrieve results
    #--------------------------------------------
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(PIPETTE_HOST, port=PIPETTE_PORT, username=USERNAME, key_filename=KEY)

        stdin, stdout, stderr = ssh.exec_command("opentrons_execute /data/"+protocol_file,get_pty=True)        # Non blocking call
        exit_status = stdout.channel.recv_exit_status()          # Blocking call,needs to wait for completition
        if exit_status == 0:                                    
            print("Pipetting operation finished. Reading results")
            try: 
                # Copying result file to local and read it
                result = subprocess.run("scp -i "+KEY+" "+USERNAME+"@"+PIPETTE_HOST+":/root/json_data.json ./json_data.json", shell=True)
                if(result.returncode==0):
                    with open('./json_data.json') as json_file:
                        data = json.load(json_file)
                      #  print(data)
                        #--------------------------------------------
                        #TODO Orion call uploading data results
                        #-------------------------------------------- 

                    print("SCP connection successful")
                    return "Operation finished"
                else:
                    print("SCP connection error. Could not copy results")
            except subprocess.CalledProcessError as e:
                print(e.output)
                return "Error copying protocol file"
        else:
            print("Error", exit_status)
        ssh.close()
    except Exception as e:
        print(e)
        ssh.close()

#------------------------------------------
# Run
#------------------------------------------
if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)