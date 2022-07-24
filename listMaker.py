import re

#funcion que elimina las keys no deseables en cada diccionario
def popper(lista):
    popperLista = lista
    for objetos in popperLista:
        objetos.pop("address",None)
        objetos.pop("configurationUpdatedAt",None)
        objetos.pop("firmware",None)
        objetos.pop("lat",None)
        objetos.pop("lng",None)
        objetos.pop("networkId",None)
        objetos.pop("notes",None)
        objetos.pop("serial",None)
        objetos.pop("tags",None)
        objetos.pop("url",None)
    return popperLista
    
#funcion que retorna una lista con los dispositivos que se quieren y con las keys que se necesitan
def listMaker(lista,palabra):

    list = []
    for objetos in lista:
        x = re.search(palabra,objetos['firmware'])

        if x:
            list.append(objetos)
        else:
            continue

    return popper(list)