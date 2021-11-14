import cv2
import numpy
from numpy.lib.function_base import iterable

def OrdenarPuntos(puntos):
    numero_puntos=numpy.concatenate(puntos[0],puntos[1],puntos[2],puntos[3]).tolist()
    
    coordenada_y=sorted(numero_puntos,key=lambda numero_puntos:numero_puntos[1])

    coordenada_x1=coordenada_y[0:2]
    coordenada_x1=sorted(coordenada_x1,key=lambda coordenada_X1:coordenada_x1[0])

    coordenada_x2=coordenada_y[2:4]
    coordenada_x2=sorted(coordenada_x2,key=lambda coordenada_x2:coordenada_x2[0])

    return [coordenada_x1[0],coordenada_x1[1],coordenada_x2[0],coordenada_x2[1]]
