import cv2
capturarVideo=cv2.VideoCapture(0)
if not capturarVideo.isOpened():
    print("No se encontró la cámara :)")
    exit()
while True:
    tipoCamara,camara=capturarVideo.read()

    escalaGris=cv2.cvtColor(camara,cv2.COLOR_BGR2GRAY)

    cv2.imshow("Camara en vivo",escalaGris)

    if cv2.waitKey(1)==ord("q"):
        break
capturarVideo.release()
cv2.destroyAllWindows()