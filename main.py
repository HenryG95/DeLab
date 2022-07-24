import requests
from getOrganizations import getOrganizations

url = "https://api.meraki.com/api/v0/organizations"

#se implementa una validacion de estado para el url de organizations
try:
    r = requests.get(url)
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