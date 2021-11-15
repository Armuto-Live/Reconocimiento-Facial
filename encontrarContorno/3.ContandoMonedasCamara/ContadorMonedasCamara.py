import cv2
import numpy
from numpy.lib.function_base import iterable
from numpy.lib.type_check import imag

def OrdenarPuntos(puntos):
    numero_puntos=numpy.concatenate(puntos[0],puntos[1],puntos[2],puntos[3]).tolist()
    
    coordenada_y=sorted(numero_puntos,key=lambda numero_puntos:numero_puntos[1])

    coordenada_x1=coordenada_y[0:2]
    coordenada_x1=sorted(coordenada_x1,key=lambda coordenada_x1:coordenada_x1[0])

    coordenada_x2=coordenada_y[2:4]
    coordenada_x2=sorted(coordenada_x2,key=lambda coordenada_x2:coordenada_x2[0])

    return [coordenada_x1[0],coordenada_x1[1],coordenada_x2[0],coordenada_x2[1]]

def Alinamiento(imagen,ancho,alto):
    imagen_alineada=None
    escala_grises=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
    tipo_umbral,umbral=cv2.threshold(escala_grises,150,255,cv2.THRESH_BINARY)
    cv2.imshow("Umbral",umbral)

    contorno,jerarquia=cv2.findContours(umbral,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
    contorno=sorted(contorno,key=cv2.ContourArea,reverse=True)[:1]

    for i in contorno:
        calibrando_ruido_curva=0.01*cv2.arcLength(i,True)
        aproximacion=cv2.approxPolyDP(i,calibrando_ruido_curva,True)
        if len(aproximacion)==4:
            puntos=OrdenarPuntos(aproximacion)
            punto1=numpy.float32(puntos)
            punto2=numpy.float32([0,0],[ancho,0],[0,alto],[ancho,alto])
            mantener_fijo=cv2.getPerspectiveTransform(punto1,punto2)
            imagen_alineada=cv2.warpPerspective(imagen,mantener_fijo,(ancho,alto))
    return imagen_alineada

url_camara="http://192.168.1.65:4747/video"

capturar_video=cv2.VideoCapture(url_camara)

while True:
    tipo_camara,camara=capturar_video.read()
    if tipo_camara==False:
        break
    
    formato_A6=Alinamiento(camara,ancho=480,alto=677)
    if formato_A6 is not None:
        puntos=[]
        imagen_gris=cv2.cvtColor(formato_A6,cv2.COLOR_BGR2GRAY)
        eliminar_ruido=cv2.GaussianBlur(imagen_gris,(5,5),1)
        _,umbral2=cv2.threshold(eliminar_ruido,0,255,cv2.THRESH_OTSU+cv2.THRESH_BINARY_INV)
        cv2.imshow("Umbralización",umbral2)

        contorno2,jerarqui2=cv2.findContours(umbral2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
        cv2.drawContours(formato_A6,contorno2,-1,(255,0,0),2)
        suma1=0.0
        suma2=0.0
        for j in contorno2:
            area=cv2.contourArea(j)
            momentos=cv2.moments(j)
            if (momentos["m00"]==0):
                momentos["m00"]==1.0
            x=int(momentos["m10"]/momentos["m00"])
            y=int(momentos[m01]/momentos["m00"])
            
        
    





