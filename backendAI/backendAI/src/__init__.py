# from crypt import methods
from urllib import response
from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from flask_restx import Api, Resource, fields, reqparse
# from werkzeug import secure_filename
from tensorflow import keras
import tensorflow as tf
import os
import cv2
import numpy as np 
import logging
import os
import json
import ast
import requests
from PIL import Image


import CellCounting as cellCounting

# print(__file__)
# print(os.path.join(os.path.dirname(__file__), '..'))
# print(os.path.dirname(os.path.realpath(__file__)))
# print(os.path.abspath(os.path.dirname(__file__)))

model = keras.models.load_model(r"../../modelo/path_to_my_model.h5",compile=False)
# model = keras.models.load_model(os.path.join("../../modelo/", 'path_to_my_model.h5'))
# model = keras.models.load_model(os.path.join("/app/modelo/", 'path_to_my_model.h5'))

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




api = Api(app=app, version="0.0.2", title="ApiBackendAI", description="ApiBackendAI")
api_namespace = api.namespace("backendAI", description="Endpoint for AI models")

loggingLevel=logging.INFO if (os.getenv('LOGGING_INFO') == "True" ) else logging.ERROR
logging.basicConfig(level=loggingLevel, format='%(asctime)s:%(levelname)s:%(message)s')



@api_namespace.route('/processImageWithLiquid',methods=["POST"])
class GetImageWithLiquid(Resource):
    #@api.expect(resource_fields)
    def post(self):
        # file = request.files['file']
        # la siguiente linea solo es para estandarizar a ascii el nombre del fichero para cuando queramos guardarlo, evitando asi posibles problemas
        # de espacios o otro tipo de caracteres extraños
        # filename = secure_filename(file.filename)
        
        # file = np.array(request.json["array"],dtype='uint8')

        # lis = ast.literal_eval(request.json["image"])
        # file = np.array(lis,dtype='uint8')

        lis = request.json["image"]
        lis = json.loads(lis)

        file = np.array(lis,dtype='uint8')

        params = {  
            'options': 'keyValues'
        }

        headers = {
            'fiware-service': 'openiot',
            'content-type': 'application/json'
        }

        responseOrion1 = request.patch(url = 'http://' + os.environ.get("ORION_HOST") + ':' + os.environ.get("ORION_PORT") + '/v2/entities/' + os.environ.get("MICROSCOPE_ENTITY_ID"),
                                        params = params,
                                        headers = headers)
        
        responseOrion1json = json.loads(responseOrion1.text)

        totalNumberOfCells = responseOrion1json['Cells']
        
        numberOfLiveCells = cellCounting.countNumberOfCellsInImage(model, file)
        cellViability = cellCounting.calculateCellViability(totalNumberOfCells, numberOfLiveCells)

        payload = {
            'image': request.json["image"],
            'numberOfLifeCells' : numberOfLiveCells,
            'cellViability' : cellViability
        }

        headers = {'content-type': 'application/json'}

        responseNotification = requests.post(url = 'http://' + os.environ.get("NOTIFICATION_HOST") + ':' + os.environ.get("NOTIFICATION_PORT") + '/api/v1/notifications/predictionWithLiquid',
                                            data=json.dumps(payload),
                                            headers=headers)

        payload = {
            'liveCells':{'type': 'Number', 'value': numberOfLiveCells},
            'cellsViability':{'type': 'Float', 'value': cellViability}
        }
        headers = {
            'fiware-service': 'openiot',
            'content-type': 'application/json'
        }

        responseOrion = requests.patch(url = 'http://' + os.environ.get("ORION_HOST") + ':' + os.environ.get("ORION_PORT") + '/v2/entities/' + os.environ.get("MICROSCOPE_ENTITY_ID") + '/attrs',
                                            data=json.dumps(payload),
                                            headers=headers)



        return make_response(jsonify(payload), 200)


@api_namespace.route('/processImageWithoutLiquid')
class GetImageWithoutLiquid(Resource):
    #@api.expect(resource_fields)
    def post(self):



        print('Llego aqui 1')

        
        # lis = ast.literal_eval(request.json["image"])
        # print('Prueba 1')
        # file = np.array(lis,dtype='uint8')
        # print('Prueba 2')

        # test = request.data
        # test = json.loads(test)
        
        lis = request.json["image"]
        lis = json.loads(lis)

        file = np.array(lis,dtype='uint8')

        totalNumberOfCells = cellCounting.countNumberOfCellsInImage(model, file)

        print(totalNumberOfCells)

        payload = {
            "image" : request.json["image"],
            "totalNumberOfCells" : str(totalNumberOfCells)
        }
        
        print('fallo aqui 1')

        headers = {'content-type': 'application/json'}

        responseNotification = requests.post(url = 'http://' + os.environ.get("NOTIFICATION_HOST") + ':' + os.environ.get("NOTIFICATION_PORT") + '/api/v1/notifications/predictionWithoutLiquid',
                                            data=json.dumps(payload),
                                            headers=headers)
        print('fallo aqui 2')
        payload = {
            'Cells':{'type': 'Number', 'value': totalNumberOfCells}
        }
        print('fallo aqui 3')
        headers = {
            'fiware-service': 'openiot',
            'content-type': 'application/json'
        }
        print('fallo aqui 4')
        responseOrion = requests.patch(url = 'http://' + os.environ.get("ORION_HOST") + ':' + os.environ.get("ORION_PORT") + '/v2/entities/' + os.environ.get("MICROSCOPE_ENTITY_ID") + '/attrs',
                                            data=json.dumps(payload),
                                            headers=headers)
        print('fallo aqui 5')
        return make_response(jsonify(payload), 200)


@app.route('/backendAI/test',methods=['POST'])
def geta():
    print("-----------------------------")
    print(request.files["file"])
    print("---------------------------")
    # file = request.files['file']
    # print(file)
    return ""
        

def main():

    # Aqui cargar los modelos, antes del app.run
    # Llamandoles de la misma forma que se pasa como argumentos en las llamadas processImageWithLiquid y processImageWithoutLiquid
    app.run(debug=True, host='0.0.0.0',port=2725)


if __name__ == '__main__':
    main()
