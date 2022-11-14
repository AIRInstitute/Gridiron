from fileinput import filename
from flask import Flask, jsonify, request, make_response, send_file
from flask_cors import CORS
from flask_restplus import Api, Resource, fields, reqparse
from PIL import Image
import numpy as np
import json
import base64
import requests

import logging
import os

from LuxConnector import LuxConnectorClass as luxConnector


app = Flask(__name__, static_url_path='')
CORS(app)


@app.errorhandler(400)
def bad_request(error):
    logging.error(error)
    return make_response(jsonify({'error': 'Bad request'}), 400)

@app.errorhandler(502)
def bad_gateway(error):
    logging.error(error)
    return make_response(jsonify({'error': 'Bad gateway'}),502)

@app.errorhandler(504)
def time_out(error):
    logging.error(error)
    return make_response(jsonify({'error': 'Time out'}),504)

@app.errorhandler(Exception)
def all_exception_handler(error):
    logging.error(f"{error}")
    return make_response(jsonify({'error': 'Internal server error'}), 500) 




api = Api(app=app, version="0.0.2", title="ApiMicroscope", description="ApiMicroscope")
api_namespace = api.namespace("microscope", description="Endpoint for the microscope")

loggingLevel=logging.INFO if (os.getenv('LOGGING_INFO') == "True" ) else logging.ERROR
logging.basicConfig(level=loggingLevel, format='%(asctime)s:%(levelname)s:%(message)s')



microscopeClient = luxConnector()

@api_namespace.route('/setFocus')
class SetFocusMicroscope(Resource):
    #@api.expect(resource_fields)
    def post(self):
        focus = microscopeClient.setFocus(request.headers['focus'])

# @api_namespace.route('/getAnImage', methods=['GET'])
# class GetAnImage(Resource):
#     #@api.expect(resource_fields)
#     def get(self):
#         image = microscopeClient.getImage()
#         image = image.convert('RGB')
#         data = np.asarray(image)
#         # img = np.array(image)
#         # lists = img.tolist()
        
#         # img = image.read()
#         # print(image[0])
#         # data = {}
#         # data['img'] = base64.b64encode(image)
#         # data['image'] = base64.encodebytes(image).decode('utf-8')

#         # return json.dumps(lists)
#         imageArray = json.dumps(data.tolist())
#         print(type(imageArray))
#         return imageArray

# @api_namespace.route('/getAnImage', methods=['POST'])
# class GetAnImage(Resource):
#     #@api.expect(resource_fields)
#     def post(self):
#         body =  request.body.decode('utf-8')
#         body = json.loads(body)
#         print(body)

#         if body['getAnImage'] == 'getImageWithoutLiquid':
#             print('entro en getImageWithoutLiquid')
#             image = microscopeClient.getImage()
#             image = image.convert('RGB')
#             data = np.asarray(image)
            
#             imageArray = json.dumps(data.tolist())

#             json_payload = {
#                 "image": imageArray
#             }

#             headers = {'Content-Type': 'application/json'}
#             response = requests.post(os.environ.get("ENDPOINT_WITHOUT_LIQUID"),
#                                     data=json.dumps(json_payload),
#                                     headers=headers)

#             return response
#         if body['getAnImage'] == 'getImageWithLiquid':
#             print('entro en getImageWithLiquid')
#             image = microscopeClient.getImage()
#             image = image.convert('RGB')
#             data = np.asarray(image)

#             imageArray = json.dumps(data.tolist())

#             json_payload = {
#                 "image": imageArray
#             }

#             headers = {'Content-Type': 'application/json'}
#             response = requests.post(os.environ.get("ENDPOINT_WITH_LIQUID"),
#                                     data=json.dumps(json_payload),
#                                     headers=headers)

#             return response


@api_namespace.route('/getAnImage', methods=['POST'])
class GetAnImage(Resource):
    #@api.expect(resource_fields)
    def post(self):
        print(request.get_json())
        print('llego aqui 1')
        # body =  request.body.decode('utf-8')
        # body = json.loads(body)
        body = request.get_json()
        print(body)
        print('entro aqui')

        if 'getImageWithoutLiquid' in body:
            print('entro en getImageWithoutLiquid')
            image = microscopeClient.getImage()
            image = image.convert('RGB')
            data = np.asarray(image)
            
            imageArray = json.dumps(data.tolist())

            json_payload = {
                "image": imageArray
            }

            headers = {'Content-Type': 'application/json'}
            response = requests.post(os.environ.get("ENDPOINT_WITHOUT_LIQUID"),
                                    data=json.dumps(json_payload),
                                    headers=headers)

            return make_response(jsonify({}), 200)
        if 'getImageWithLiquid' in body:
            print('entro en getImageWithLiquid')
            image = microscopeClient.getImage()
            image = image.convert('RGB')
            data = np.asarray(image)

            imageArray = json.dumps(data.tolist())

            json_payload = {
                "image": imageArray
            }

            headers = {'Content-Type': 'application/json'}
            response = requests.post(os.environ.get("ENDPOINT_WITH_LIQUID"),
                                    data=json.dumps(json_payload),
                                    headers=headers)

            return make_response(jsonify({}, 200))


@api_namespace.route('/getImageWithoutLiquid', methods=['POST'])
class GetImageWithoutLiquid(Resource):
    #@api.expect(resource_fields)
    def post(self):

        print('entro en getImageWithoutLiquid')
        image = microscopeClient.getImage()
        image = image.convert('RGB')
        data = np.asarray(image)
        
        imageArray = json.dumps(data.tolist())

        json_payload = {
            "image": imageArray
        }

        headers = {'Content-Type': 'application/json'}
        response = requests.post(os.environ.get("ENDPOINT_WITHOUT_LIQUID"),
                                data=json.dumps(json_payload),
                                headers=headers)

        return response
        

@api_namespace.route('/getImageWithLiquid', methods=['POST'])
class GetAnImage(Resource):
    #@api.expect(resource_fields)
    def post(self):

        print('entro en getImageWithLiquid')
        image = microscopeClient.getImage()
        image = image.convert('RGB')
        data = np.asarray(image)

        imageArray = json.dumps(data.tolist())

        json_payload = {
            "image": imageArray
        }

        headers = {'Content-Type': 'application/json'}
        response = requests.post(os.environ.get("ENDPOINT_WITH_LIQUID"),
                                data=json.dumps(json_payload),
                                headers=headers)

        return response

@api_namespace.route('/getAnImageWithoutLiquid', methods=['GET','POST'])
class GetAnImageWithoutLiquid(Resource):
    #@api.expect(resource_fields)
    def post(self):
        image = microscopeClient.getImage()
        image = image.convert('RGB')
        data = np.asarray(image)
        # img = np.array(image)
        # lists = img.tolist()
        
        # img = image.read()
        # print(image[0])
        # data = {}
        # data['img'] = base64.b64encode(image)
        # data['image'] = base64.encodebytes(image).decode('utf-8')

        # return json.dumps(lists)
        imageArray = json.dumps(data.tolist())

        json_payload = {
            "image": imageArray
        }

        headers = {'Content-Type': 'application/json'}
        response = requests.post(os.environ.get("ENDPOINT_WITHOUT_LIQUID"),
                                data=json.dumps(json_payload),
                                headers=headers)

        return response

@api_namespace.route('/getAnImageWithLiquid', methods=['POST'])
class GetAnImageWithLiquid(Resource):
    #@api.expect(resource_fields)
    def post(self):
        image = microscopeClient.getImage()
        image = image.convert('RGB')
        data = np.asarray(image)
        # img = np.array(image)
        # lists = img.tolist()
        
        # img = image.read()
        # print(image[0])
        # data = {}
        # data['img'] = base64.b64encode(image)
        # data['image'] = base64.encodebytes(image).decode('utf-8')

        # return json.dumps(lists)
        imageArray = json.dumps(data.tolist())

        json_payload = {
            "image": imageArray
        }

        headers = {'Content-Type': 'application/json'}
        response = requests.post(os.environ.get("ENDPOINT_WITH_LIQUID"),
                                data=json.dumps(json_payload),
                                headers=headers)

        return response


@api_namespace.route('/getTemperature', methods=['GET'])
class GetTemperature(Resource):
    #@api.expect(resource_fields)
    def get(self):
        return microscopeClient.getTemperature()

@api_namespace.route('/getSerialNumber', methods=['GET'])
class GetSerialNumber(Resource):
    #@api.expect(resource_fields)
    def get(self):
        return microscopeClient.getSerialNumber()


#Todavía por completar
@api_namespace.route('/getStack', methods=['GET'])
class GetStack(Resource):
    #@api.expect(resource_fields)
    def get(self):
        return microscopeClient.getStack(request.headers['num_img'], request.headers['start_focus'], request.headesrs['end_focus'])       


def main():
    app.run(debug=True, host='0.0.0.0',port=5000)


if __name__ == '__main__':
    main()