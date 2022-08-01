#Se importan las librerias
#Se importa matplotlib y pylab para graficar los datos. Luego csv para poder tomar los datos
from pylab import *
import matplotlib.pyplot as plt
import csv as c
#Se le pide al usuario que seleccione una de tres opciones
inicio = int(input('Selecciona la decada 2000-2010, 2010-2020 ó 2020-2030. ¿1, 2 ó 3? '))
#Se abre el archivo csv con la data de las 3 decadas para los graficos
filename = "data.csv"
#mantenemos abierto el archivo csv para las consultas de datos
with open(filename) as f:
    reader = c.reader(f)
#creamos un condicional donde se ejecuta segun la respuesta
    if inicio==1:
        valores = []
        for row in reader:
            valor = int(row[1])
            valores.append(valor)
        plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.plot(valores, c="red")
        plt.title('Grafico de ventas en la decada 2000-2010')
        plt.xlabel('AÑOS')
        plt.show()
    if inicio==2:
        valores = []
        for row in reader:
            valor = int(row[2])
            valores.append(valor)
        plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.plot(valores, c="blue")
        plt.title('Grafico de ventas en la decada 2010-2020')
        plt.xlabel('AÑOS')
        plt.show()
    if inicio==3:
        valores = []
        for row in reader:
            valor = int(row[3])
            valores.append(valor)
        #Usamos estilos de plt
        plt.style.use('seaborn')
        fig, ax = plt.subplots()
        #le damos color al grafico
        ax.plot(valores, c="green")
        #Le damos identificacion al grafico
        plt.title('Grafico de ventas en la decada 2020-2030')
        #Identificamos el eje x
        plt.xlabel('AÑOS')
        #mostramos el grafico en pantalla
        plt.show()