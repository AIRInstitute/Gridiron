import json
import cv2
import numpy as np
import math
from PIL import Image
import tensorflow as tf
from flask import Flask, request, Response

# Define the helper function
def decode_segmap(image, nc=21):
    label_colors = np.array([(0, 0, 0),  # 0=background
               # 1=aeroplane, 2=bicycle, 3=bird, 4=boat, 5=bottle
               (128, 0, 0), (0, 128, 0), (128, 128, 0), (0, 0, 128), (128, 0, 128),
               # 6=bus, 7=car, 8=cat, 9=chair, 10=cow
               (0, 128, 128), (128, 128, 128), (64, 0, 0), (192, 0, 0), (64, 128, 0),
               # 11=dining table, 12=dog, 13=horse, 14=motorbike, 15=person
               (192, 128, 0), (64, 0, 128), (192, 0, 128), (64, 128, 128), (192, 128, 128),
               # 16=potted plant, 17=sheep, 18=sofa, 19=train, 20=tv/monitor
               (0, 64, 0), (128, 64, 0), (0, 192, 0), (128, 192, 0), (0, 64, 128)])

    r = np.zeros_like(image).astype(np.uint8)
    g = np.zeros_like(image).astype(np.uint8)
    b = np.zeros_like(image).astype(np.uint8)
  
    for l in range(0, nc):
        idx = image == l
        r[idx] = label_colors[l, 0]
        g[idx] = label_colors[l, 1]
        b[idx] = label_colors[l, 2]
    
    rgb = np.stack([r, g, b], axis=2)
    return rgb

# Define the helper function
def numCells(image,minimum_area= 1,average_cell_area= 250,connected_cell_area = 100):
    rgb_1 = decode_segmap(image[-1,:,:,-1])
    rgb = cv2.cvtColor(rgb_1, cv2.COLOR_BGR2GRAY)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
    opening = cv2.morphologyEx(rgb, cv2.MORPH_OPEN, kernel, iterations=1)
    close = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel, iterations=2)
    cnts = cv2.findContours(close, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    cells = 0
    for c in cnts:
        area = cv2.contourArea(c)
        if area > minimum_area:
            cv2.drawContours(rgb, [c], -1, (36,255,12), 2)
            if area > connected_cell_area:
                cells += math.ceil(area / average_cell_area)
            else:
                cells += 1
    return cells

def countNumberOfCellsInImage(model, image):


    
    print('Llego aqui 1')
    img_real = cv2.resize(image,(256,256))
    print('Llego aqui 2')
    segCells=model.predict(np.expand_dims(img_real, axis = 0), batch_size=None, verbose=0, steps=None, callbacks=None)
    print('Llego aqui 3')


    numberOfCells = numCells(segCells,minimum_area= 1,average_cell_area= 250,connected_cell_area = 100) #En esta linea sustituir el model.predict por model. cual sea el metodo que se usa para contar el numero de celulas en una imagen (model es el modelo ya entreando)

    print('Llego aqui 4')

    return numberOfCells


def calculateCellViability(totalNumberOfCells, numberOfLiceCells):

    cellViability = 0
    if(totalNumberOfCells != 0):
        cellViability = (numberOfLiceCells/totalNumberOfCells)*100
    
    

    return cellViability

