import cv2
imagen=cv2.imread('cuadrado.jpg')
escalaGris=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
_,umbral=cv2.threshold(escalaGris,225,255,cv2.THRESH_BINARY)
contornos,jerarquia=cv2.findContours(umbral,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imagen,contornos,-1,(255,0,0),3)

print(cv2.drawContours)

cv2.imshow("Escala de grises",escalaGris)
cv2.imshow("umbral",umbral)
cv2.imshow('Imagen original',imagen)
cv2.waitKey(0)