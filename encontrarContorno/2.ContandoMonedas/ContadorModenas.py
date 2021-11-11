import cv2
import numpy

kernelGaussiano=1
valorKernel=7

imagenOriginal=cv2.imread("monedas.jpg")
escalaGris=cv2.cvtColor(imagenOriginal,cv2.COLOR_BGR2GRAY)
desenfoque=cv2.GaussianBlur(escalaGris,(kernelGaussiano,kernelGaussiano),0)
canny=cv2.Canny(desenfoque,500,10)
kernel=numpy.ones((valorKernel,valorKernel),numpy.uint8)
clausura=cv2.morphologyEx(canny,cv2.MORPH_CLOSE,kernel)

contorno,jerarquia=cv2.findContours(clausura.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imagenOriginal,contorno,-1,(0,255,0),2)

print("La cantidad de monedas son:{}".format(len(contorno)))


cv2.imshow("Imagen a escala de gris",escalaGris)
cv2.imshow("desenfoque",desenfoque)
cv2.imshow("canny",canny)
cv2.imshow("clausura",clausura)
cv2.imshow("Imagen Original",imagenOriginal)
cv2.waitKey(0)