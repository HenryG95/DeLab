import requests,json

#función para listar todas las organizaciones a las que se tiene acceso con el API Key
def getOrganizations(headers,payload,url):

    r = requests.get(url)


    response = requests.request('GET', url, headers=headers, data = payload)

    return json.loads(response.text)

