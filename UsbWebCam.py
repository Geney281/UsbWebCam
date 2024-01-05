import cv2 # opencv
import sys # Parámetros y funciones específicos del sistema

cap = cv2.VideoCapture(0) # Crear objeto VideoCapture



while(True):
    ret, frame = cap.read()# Captura de frame

    if ret: # Verificar si ha leído correctamente.
        cv2.imshow('Visual',frame) # Mostrar el frame.
    else:
        print("Usb Cam disconnected")
        break
    
    # Mostrar frame por 1ms y verificar si tecla ingresada es Esc   
    if (cv2.waitKey(1) & 0xFF == 27):
        break

cap.release()# Liberar la captura
cv2.destroyAllWindows()# Destruir las ventanas
