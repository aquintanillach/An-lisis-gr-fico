import numpy as np
import cv2
#Esto es un repaso de la importación de datos gráficos para su posterior análisis.
##A partir de una micrografía microscópica se pretende  encontrar las bacterias capaces de crear una infección en la garganta a partir de eridas o bajas defensas
##La tensión de gram es un fenómeno muy cotidiano en las infecciones y muy estudiado especialmente para los niños, ya que estos sufren infecciones eguidas y es prioritario encontrar cual es la bacteria causante de su infección

#Importar datos de figuras
#LLamar la imagen dentro de mi código

im0 = cv2.imread('tinciondegram.jpg') #im0 es una variable que va a cargar
im1 = cv2.cvtColor(im0, cv2.COLOR_BGR2GRAY) #Pasar las matrices de datos a colores

##Contornos aplicando condicionales
ret, thresh = cv2.threshold(im1, 127, 255, 0)

cont, hie = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

print(hie)
#print(thresh)
cv2.drawContours(im0, cont, -1, (0,255,0),3)

##Mostrar el resultado

cv2.imshow('Imagen Original', im0)
cv2.imshow('Imagen Grises', im1)
cv2.waitKey(0)
cv2.destroidAllWindows()

print(im0)

