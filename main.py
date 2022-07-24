import requests
from get import get
from listMaker import listMaker
from csvMaker import csvMaker

url = "https://api.meraki.com/api/v0/organizations"
url_devices = "https://api.meraki.com/api/v0/organizations/681155/devices"

#se implementa una validacion de estado para el url de organizations
try:
    r = requests.get(url_devices)
    r.raise_for_status()
except requests.exceptions.HTTPError as err:
    print("Codigo de Estado Malo", r.status_code)

#informacion de payload y headers
payload = None

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
}

#se crea una lista de todos los dispositivos de la compañia deLab
deLab = get(headers,payload,url_devices)
#se crea una lista especifica de los dispositivos que se necesitan
listaDeseada = listMaker(deLab,"wireless|wired")
#se crea un archivo csv de la lista deseada
csvMaker(listaDeseada)


