from email import header
import logging
import os
from urllib import request
from wsgiref import headers
import requests
import json
from rest_framework.exceptions import APIException

from django.conf import settings
from django.http import HttpResponse, JsonResponse

logger = logging.getLogger(__name__)

class KeyrockClient(object):


    def get_token(self,keystone_url):
        logging.debug('getting token...')

        # json_payload = {
        #     "auth": {
        #         "identity": {
        #             "methods": ["password"],
        #             "password": {
        #                 "user": {
        #                     "name": "admin@test.com",
        #                     "domain": {"id": "default"},
        #                     "password": "1234"
        #                 }
        #             }
        #         }
        #     }
        # }

        json_payload = {
            "name": "admin@test.com",
            "password": "1234"
        }

        # print('http://' + keystone_url + '/v1/auth/tokens')
        headers = {'Content-Type': 'application/json'}
        response = requests.post('http://' + keystone_url + '/v1/auth/tokens',
        # response = requests.post(url=keystone_url + '/v3/auth/tokens',
                                data=json.dumps(json_payload),
                                headers=headers)

        if response.status_code in (201, 200):
            token = response.headers['X-Subject-Token']
            logging.info('TOKEN --- ' + token)
            return token
        else:
            logging.error('GET TOKEN ### ' + response.text)
    

    # def get_token_oauth(self):

    def get_token_oauth(self,keystone_url, body):
        logging.debug('getting token...')
        print(body)
        body = json.loads(body)

        json_payload = {
            "grant_type": "password",
            "username": body['name'],
            "password": body['password']
        }
        print(json_payload)

        # print('http://' + keystone_url + '/v1/auth/tokens')
        headers = {
            'Authorization': body['authorization'],
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'aplication/json'
        }
        response = requests.post('http://' + keystone_url + '/oauth2/token',
        # response = requests.post(url=keystone_url + '/v3/auth/tokens',
                                data=json_payload,
                                headers=headers)

        # if response.status_code in (201, 200):
        #     return response
        # else:
        #     logging.error('GET TOKEN ### ' + response.text)

        return response


    def get_user_info(self, keystone_url, token, user_id):

        headers = {'X-Auth-token': token}

        response = requests.get(url = 'http://' + keystone_url + '/v1/users/' + user_id,
                                headers=headers)

        if response.status_code in (201, 200):
            # parsed = json.loads(response.text)
            # logging.info(json.dumps(parsed, indent=4, sort_keys=True))
            return response
        else:
            logging.error('GET USER INFO ### ' + response.text)

    
    def update_user(self, keystone_url, token, user_id, body):

        headers = {'Content-Type': 'application/json', 'X-Auth-token': token}

        body = json.loads(body)

        json_payload = {
            "user": {
                "username": body['user']['username'],
                "email": body['user']['email'],
                "enabled": body['user']['enabled'],
                "gravatar": body['user']['gravatar'],
                "date_password": body['user']['date_password'],
                "description": body['user']['description'],
                "website": body['user']['website']
            }
        }

        response = requests.patch(url = 'http://' + keystone_url + '/v1/users/' + user_id,
                                data=json.dumps(json_payload),
                                headers=headers)

        if response.status_code in (201, 200):
            # parsed = json.loads(response.text)
            # logging.info(json.dumps(parsed, indent=4, sort_keys=True))
            return response
        else:
            logging.error('GET USER INFO ### ' + response.text)


    def list_roles(self, keystone_url, token):
        headers = {'X-Auth-token': token}

        response = requests.get(url=keystone_url + '/v3/OS-ROLES/roles',
                                headers=headers)

        if response.status_code in (201, 200):
            parsed = json.loads(response.text)
            logging.info(json.dumps(parsed, indent=4, sort_keys=True))
            return parsed
        else:
            logging.error('LIST ROLES ### ' + response.text)


    def list_permissions(self, keystone_url, token):
        headers = {'X-Auth-token': token}

        response = requests.get(url=keystone_url + '/v3/OS-ROLES/permissions',
                                headers=headers)

        if response.status_code in (201, 200):
            parsed = json.loads(response.text)
            logging.info(json.dumps(parsed, indent=4, sort_keys=True))
            return parsed
        else:
            logging.error('LIST PERMISSIONS ### ' + response.text)


    def get_role(self, role_id, keystone_url, token):
        headers = {'X-Auth-token': token}

        response = requests.get(url=keystone_url + '/v3/OS-ROLES/roles/' + role_id,
                                headers=headers)

        if response.status_code in (201, 200):
            parsed = json.loads(response.text)
            logging.info(json.dumps(parsed, indent=4, sort_keys=True))
            return parsed
        else:
            logging.error('LIST ROLE PERMISSIONS ### ' + response.text)


    def role_permissions(self, role_id, keystone_url, token):
        headers = {'X-Auth-token': token}

        response = requests.get(url=keystone_url + '/v3/OS-ROLES/roles/' + role_id + '/permissions',
                                headers=headers)

        if response.status_code in (201, 200):
            parsed = json.loads(response.text)
            logging.info(json.dumps(parsed, indent=4, sort_keys=True))
            return parsed
        else:
            logging.error('LIST ROLE PERMISSIONS ### ' + response.text)


    def put_permissions_in_role(self, role_id, permissions_id, keystone_url, token):
        headers = {'X-Auth-token': token}

        response = requests.put(url=keystone_url + '/v3/OS-ROLES/roles/' + role_id + '/permissions/' + permissions_id + '',
                                headers=headers)

        if response.status_code in (201, 200):
            parsed = json.loads(response.text)
            logging.info(json.dumps(parsed, indent=4, sort_keys=True))
            return parsed
        else:
            logging.error('LIST ROLE ORGANIZATION ### ' + response.text)


    def delete_permissions(self, id_p, keystone_url, token):
        headers = {'X-Auth-token': token}

        response = requests.delete(url=keystone_url + '/v3/OS-ROLES/permissions/' + id_p,
                                headers=headers)

        if response.status_code in (201, 200):
            parsed = json.loads(response.text)
            logging.info(json.dumps(parsed, indent=4, sort_keys=True))
            return parsed
        else:
            logging.error('LIST ROLE ORGANIZATION ### ' + response.text)


    def delete_users(self, keystone_url, token, id_user):
        headers = {'X-Auth-token': token}

        response = requests.delete(url = 'http://' + keystone_url + '/v1/users/' + id_user,
                                headers=headers)

        if response.status_code in (201, 200):
            # parsed = json.loads(response.text)
            # logging.info(json.dumps(parsed, indent=4, sort_keys=True))
            return response
        else:
            logging.error('DELETE USER ### ' + response.text)


    def delete_role(self, id_role, keystone_url, token):
        headers = {'X-Auth-token': token}

        response = requests.delete(url=keystone_url + '/v3/OS-ROLES/roles/' + id_role,
                                headers=headers)

        if response.status_code in (201, 200):
            parsed = json.loads(response.text)
            logging.info(json.dumps(parsed, indent=4, sort_keys=True))
            return parsed
        else:
            logging.error('DELE ROLE ### ' + response.text)


    def list_users_roles(self, keystone_url, token):
        headers = {'X-Auth-token': token}

        response = requests.get(url=keystone_url + '/v3/OS-ROLES/users/role_assignments',
                                headers=headers)

        if response.status_code in (201, 200):
            parsed = json.loads(response.text)
            logging.info(json.dumps(parsed, indent=4, sort_keys=True))
            return parsed
        else:
            logging.error('LIST ROLES ### ' + response.text)


    def list_users(self, keystone_url, token):
        headers = {'X-Auth-token': token}

        response = requests.get(url = 'http://' + keystone_url + '/v1/users',
                                headers=headers)

        if response.status_code in (201, 200):
            # parsed = json.loads(response.text)
            # logging.info(json.dumps(parsed, indent=4, sort_keys=True))
            return response
        else:
            logging.error('LIST USERS ### ' + response.text)


    def create_user(self, keystone_url, token, body):
        
        # json_payload = {
        #     "userName": "user1",
        #     "displayName": "user1",
        #     "password": "1234",
        #     "emails": [
        #         {
        #             "value": "user1@gmail.com"
        #         }
        #     ]
        # }

        body = json.loads(body)

        json_payload = {
            "user": {
                "username": body['user']['username'],
                "admin": body['user']['admin'],
                "password": body['user']['password'],
                "email": body['user']['email']
            }
        }

        headers = {'X-Auth-token': token, 'Content-Type': 'application/json'}
        response = requests.post(url='http://' + keystone_url + '/v1/Users/',
        # response = requests.post(url=keystone_url + '/v3/OS-SCIM/v2/Users/',
                                data=json.dumps(json_payload),
                                headers=headers)

        if response.status_code in (201, 200):
            logging.info(response.text)
            return HttpResponse(response)
        else:
            logging.error(response.text)

        # return HttpResponse(response)


    def create_role(self, keystone_url, token):
        json_payload = {
            "role": {
                "name": "developer",
                "application_id": "9d334951789a433d8bcff3d5334eee84"
            }
        }

        headers = {'X-Auth-token': token, 'Content-Type': 'application/json'}
        response = requests.post(url=keystone_url + '/v3/OS-ROLES/roles',
                                data=json.dumps(json_payload),
                                headers=headers)

        if response.status_code in (201, 200):
            logging.info(response.text)
        else:
            logging.error(response.text)


    def create_polices(self, keystone_url, token):
        json_payload = {
            "permission": {
                "name": "list users",
                "application_id": "9d334951789a433d8bcff3d5334eee84",
                "resource": "service2/list",
                "action": "GET",
            }
        }

        headers = {'X-Auth-token': token, 'Content-Type': 'application/json'}
        response = requests.post(url=keystone_url + '/v3/OS-ROLES/permissions',
                                data=json.dumps(json_payload),
                                headers=headers)

        if response.status_code in (201, 200):
            logging.info(response.text)
        else:
            logging.error(response.text)


    def put_role_in_user(self, user_id, application_id, role_id, keystone_url, token):
        headers = {'X-Auth-token': token}

        response = requests.put(
            url=keystone_url + '/v3/OS-ROLES/users/' + user_id + '/applications/' + application_id + '/roles/' + role_id,
            headers=headers)

        if response.status_code in (201, 200):
            parsed = json.loads(response.text)
            logging.info(json.dumps(parsed, indent=4, sort_keys=True))
            return parsed
        else:
            logging.error('PUT ROLE IN USER ### ' + response.text)


class OrionClient(object):

    def get_entities(self):

        params = {
            'options': 'keyValues'
        }

        response = requests.get(url = 'http://' + f"{settings.ORION_HOST}:{settings.ORION_PORT}" + '/v2/entities/', params = params)

        return response

    def get_entity_by_id(self, urn):


        params = {
            'options': 'keyValues'
        }
        
        headers = {
            'fiware-service': '',
            'fiware-servicepath': '/'
        }

        response = requests.get(url = 'http://' + f"{settings.ORION_HOST}:{settings.ORION_PORT}" + '/v2/entities/' + urn, 
                                params = params,
                                headers = headers)

        return response

    def get_complete_entity_by_id(self, urn):

        response = requests.get(url = 'http://' + f"{settings.ORION_HOST}:{settings.ORION_PORT}" + '/v2/entities/' + urn)

        return response
    
    def get_image_without_liquid(self):

        # microscopeEntity = self.get_entity_by_id("urn:ngsi-ld:microscope")
        # microscopeEntity = microscopeEntity.json()

        # if microscopeEntity['getImageWithoutLiquid'] == 0:
        #     command = 1
        # else:
        #     command = 0
        
        # payload = {
        #     "getImageWithoutLiquid": {
        #         "type": "Number",
        #         "value": command
        #     }
        # }

        payload = {
            "getImageWithoutLiquid": {
                "type": "command",
                "value": ""
            }
        }

        headers = {
            'Content-Type': 'application/json',
            'fiware-service': f"{settings.FIWARE_SERVICE}",
            'fiware-servicepath': f"{settings.FIWARE_SERVICEPATH}"
        }

        response = requests.patch(url = 'http://' + f"{settings.ORION_HOST}:{settings.ORION_PORT}" + '/v2/entities/' + f"{settings.MICROSCOPE_ENTITY_ID}" + '/attrs',
                                data = json.dumps(payload),
                                headers = headers)

        return JsonResponse({'command': 'OK'}, status = 200)

    def get_image_with_liquid(self):

        # microscopeEntity = self.get_entity_by_id("urn:ngsi-ld:microscope")
        # microscopeEntity = microscopeEntity.json()

        # if microscopeEntity['getImageWithLiquid'] == 0:
        #     command = 1
        # else:
        #     command = 0
        
        # payload = {
        #     "getImageWithLiquid": {
        #         "type": "Number",
        #         "value": command
        #     }
        # }

        payload = {
            "getImageWithLiquid": {
                "type": "command",
                "value": ""
            }
        }

        headers = {
            'Content-Type': 'application/json',
            'fiware-service': f"{settings.FIWARE_SERVICE}",
            'fiware-servicepath': f"{settings.FIWARE_SERVICEPATH}"
        }

        response = requests.patch(url = 'http://' + f"{settings.ORION_HOST}:{settings.ORION_PORT}" + '/v2/entities/' + f"{settings.MICROSCOPE_ENTITY_ID}" + '/attrs',
                                data = json.dumps(payload),
                                headers = headers)

        return JsonResponse({'command': 'OK'}, status = 200)

    def execute_first_protocol(self, bodyRequest):

        body = json.loads(bodyRequest)

        pipetteEntity = self.get_entity_by_id("urn:ngsi-ld:pipette")
        pipetteEntity = pipetteEntity.json()

        if pipetteEntity['executeProtocol'] == 0:
            command = 1
        else:
            command = 0
        
        payloadOrion = {
            # "executeProtocol": {
            #     "type": "Number",
            #     "value": command
            # },
            # "protocol": {
            #     "type": "Number",
            #     "value": 1,
            # },
            "n_falcons_15ml": {
                "type": "Number",
                "value": body['value']['n_falcons_15ml']
            },
            "n_eppendorfs": {
                "type": "Number",
                "value": body['value']['n_eppendorfs']
            },
            "starting_v_falcon": {
                "type": "Number",
                "value": body['value']['starting_v_falcon']
            },
            "volume_falcons": {
                "type": "structuredValue",
                "value": body['value']['volume_falcons']
            }
        }

        payloadAgent = {
            "actionType": "update",
            "entities": [
                {
                    "type": "pipette",
                    "id": os.environ.get("PIPETTE_ENTITY_ID"),
                    "protocol1": {
                        "type": "command",
                        "value": payloadOrion
                    }
                }
            ]
            
        }

        headers = {
            'Content-Type': 'application/json',
            'fiware-service': 'openiot',
            'fiware-servicepath': '/'
        }

        responseOrion = requests.patch(url = 'http://' + f"{settings.ORION_HOST}:{settings.ORION_PORT}" + '/v2/entities/urn:ngsi-ld:pipette/attrs',
                                data = json.dumps(payloadOrion),
                                headers = headers)

        responseAgent = requests.post(url = 'http://' + os.environ.get("AGENT_HOST") + ':' + os.environ.get("AGENT_PORT") + '/v2/op/update',
                                data = json.dumps(payloadAgent),
                                headers=headers)

        return JsonResponse({'command': 'OK'}, status = 200)

    def execute_second_protocol(self, bodyRequest):

        body = json.loads(bodyRequest)

        pipetteEntity = self.get_entity_by_id("urn:ngsi-ld:pipette")
        pipetteEntity = pipetteEntity.json()

        if pipetteEntity['executeProtocol'] == 0:
            command = 1
        else:
            command = 0
        
        payloadOrion = {
            # "executeProtocol": {
            #     "type": "Number",
            #     "value": command
            # },
            # "protocol": {
            #     "type": "Number",
            #     "value": 2,
            # },
            "n_eppendorfs": {
                "type": "Number",
                "value": body['value']['n_eppendorfs']
            },
            "starting_v_falcon_B4": {
                "type": "Number",
                "value": body['value']['starting_v_falcon_B4']
            }
        }

        payloadAgent = {
            "actionType": "update",
            "entities": [
                {
                    "type": "pipette",
                    "id": os.environ.get("PIPETTE_ENTITY_ID"),
                    "protocol2": {
                        "type": "command",
                        "value": payloadOrion
                    }
                }
            ]
            
        }

        headers = {
            'Content-Type': 'application/json',
            'fiware-service': 'openiot',
            'fiware-servicepath': '/'
        }

        responseOrion = requests.patch(url = 'http://' + f"{settings.ORION_HOST}:{settings.ORION_PORT}" + '/v2/entities/urn:ngsi-ld:pipette/attrs',
                                data = json.dumps(payloadOrion),
                                headers = headers)

        responseAgent = requests.post(url = 'http://' + os.environ.get("AGENT_HOST") + ':' + os.environ.get("AGENT_PORT") + '/v2/op/update',
                                data = json.dumps(payloadAgent),
                                headers=headers)

        return JsonResponse({'command': 'OK'}, status = 200)

    def execute_third_protocol(self, bodyRequest):

        body = json.loads(bodyRequest)

        pipetteEntity = self.get_entity_by_id("urn:ngsi-ld:pipette")
        pipetteEntity = pipetteEntity.json()

        if pipetteEntity['executeProtocol'] == 0:
            command = 1
        else:
            command = 0
        
        payloadOrion = {
            # "executeProtocol": {
            #     "type": "Number",
            #     "value": command
            # },
            # "protocol": {
            #     "type": "Number",
            #     "value": 3,
            # },
            "n_wellplates": {
                "type": "Number",
                "value": body['value']['n_wellplates']
            },
            "n_falcons_50ml": {
                "type": "Number",
                "value": body['value']['n_falcons_50ml']
            },
        }

        payloadAgent = {
            "actionType": "update",
            "entities": [
                {
                    "type": "pipette",
                    "id": os.environ.get("PIPETTE_ENTITY_ID"),
                    "protocol3": {
                        "type": "command",
                        "value": payloadOrion
                    }
                }
            ]
            
        }

        headers = {
            'Content-Type': 'application/json',
            'fiware-service': 'openiot',
            'fiware-servicepath': '/'
        }

        responseOrion = requests.patch(url = 'http://' + f"{settings.ORION_HOST}:{settings.ORION_PORT}" + '/v2/entities/urn:ngsi-ld:pipette/attrs',
                                data = json.dumps(payloadOrion),
                                headers = headers)

        responseAgent = requests.post(url = 'http://' + os.environ.get("AGENT_HOST") + ':' + os.environ.get("AGENT_PORT") + '/v2/op/update',
                                data = json.dumps(payloadAgent),
                                headers=headers)

        return JsonResponse({'command': 'OK'}, status = 200)

    def execute_fourth_protocol(self, bodyRequest):

        body = json.loads(bodyRequest)

        pipetteEntity = self.get_entity_by_id("urn:ngsi-ld:pipette")
        pipetteEntity = pipetteEntity.json()

        if pipetteEntity['executeProtocol'] == 0:
            command = 1
        else:
            command = 0
        
        payloadOrion = {
            # "executeProtocol": {
            #     "type": "Number",
            #     "value": command
            # },
            # "protocol": {
            #     "type": "Number",
            #     "value": 4,
            # },
            "n_cuvettes": {
                "type": "Number",
                "value": body['value']['n_cuvettes']
            },
        }

        payloadAgent = {
            "actionType": "update",
            "entities": [
                {
                    "type": "pipette",
                    "id": os.environ.get("PIPETTE_ENTITY_ID"),
                    "protocol4": {
                        "type": "command",
                        "value": payloadOrion
                    }
                }
            ]
            
        }

        headers = {
            'Content-Type': 'application/json',
            'fiware-service': 'openiot',
            'fiware-servicepath': '/'
        }

        responseOrion = requests.patch(url = 'http://' + f"{settings.ORION_HOST}:{settings.ORION_PORT}" + '/v2/entities/urn:ngsi-ld:pipette/attrs',
                                data = json.dumps(payloadOrion),
                                headers = headers)
        
        responseAgent = requests.post(url = 'http://' + os.environ.get("AGENT_HOST") + ':' + os.environ.get("AGENT_PORT") + '/v2/op/update',
                                data = json.dumps(payloadAgent),
                                headers=headers)

        return JsonResponse({'command': 'OK'}, status = 200)

    def execute_fifth_protocol(self, bodyRequest):

        body = json.loads(bodyRequest)

        pipetteEntity = self.get_entity_by_id("urn:ngsi-ld:pipette")
        pipetteEntity = pipetteEntity.json()

        if pipetteEntity['executeProtocol'] == 0:
            command = 1
        else:
            command = 0
        
        payloadOrion = {
            # "executeProtocol": {
            #     "type": "Number",
            #     "value": command
            # },
            # "protocol": {
            #     "type": "Number",
            #     "value": 5,
            # },
            "n_cuvettes": {
                "type": "Number",
                "value": body['value']['n_cuvettes']
            }

        }

        payloadAgent = {
            "actionType": "update",
            "entities": [
                {
                    "type": "pipette",
                    "id": os.environ.get("PIPETTE_ENTITY_ID"),
                    "protocol5": {
                        "type": "command",
                        "value": payloadOrion
                    }
                }
            ]
            
        }

        headers = {
            'Content-Type': 'application/json',
            'fiware-service': 'openiot',
            'fiware-servicepath': '/'
        }

        responseOrion = requests.patch(url = 'http://' + f"{settings.ORION_HOST}:{settings.ORION_PORT}" + '/v2/entities/urn:ngsi-ld:pipette/attrs',
                                data = json.dumps(payloadOrion),
                                headers = headers)

        responseAgent = requests.post(url = 'http://' + os.environ.get("AGENT_HOST") + ':' + os.environ.get("AGENT_PORT") + '/v2/op/update',
                                data = json.dumps(payloadAgent),
                                headers=headers)

        return JsonResponse({'command': 'OK'}, status = 200)
