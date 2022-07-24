import requests,json

#función que retorna una lista de la informacion que se pide que tiene acceso con el API Key
def get(headers,payload,url):

    response = requests.request('GET', url, headers=headers, data = payload)

    return json.loads(response.text)

