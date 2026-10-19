# Importamos las librerias
import cv2
import matplotlib.pyplot as plt
import os
#ruta de la imagen
ruta_imagen = os.path.join(
    "img-original-0120",
    "img-jeep-0120.jpg"
)
# Imagen
# Vamos a crear nuestra matriz principal
jeep = cv2.imread(ruta_imagen)
#print(jeep) muestra las matrices de la imagen
# Convertir de BGR a RGB color rojo COLOR_BGR
jp = cv2.cvtColor(jeep, cv2.COLOR_BGR2RGB)
#cv2.imshow("jeep original 0120",jeep)
cv2.imshow("jeep color 0120", jp)
cv2.waitKey(0) # tiempo de espera
cv2.destroyAllWindows() # destruye todas las ventanas en memoriac