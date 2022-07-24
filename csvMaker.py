import csv
from unicodedata import name

fieldnames = ['lanIp','mac','model','name','wan1Ip','wan2Ip']
 #funcion que crea un archivo csv ordenado como indica la lista de arriba
def csvMaker(lista):

    with open('dispositivos.csv','w',encoding='UTF8',newline='') as f:
        writer = csv.DictWriter(f,fieldnames=fieldnames)
        writer.writerows(lista)