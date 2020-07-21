import requests
import json
apikey_import_= {
    'api_key': 'RGAPI-1d4d4070-264d-41f5-8a39-16a057126588'
}

def verificar_status(game_region):
    status_respuesta = requests.get("https://{}.api.riotgames.com/lol/status/v3/shard-data".format(game_region),params=apikey_import_)
    status_respuesta_json = status_respuesta.json()

    status_server = status_respuesta_json["services"][0]["status"]
    if status_server != "online":
        return 0
    else:
        return 1

    if status_respuesta == 503:
        return 'HTTP GET Error, Service unavailable'


def Mensajes_RIOT(game_region):
    status_respuesta = requests.get("https://{}.api.riotgames.com/lol/status/v3/shard-data".format(game_region), params=apikey_import_)
    status_respuesta_json = status_respuesta.json()

    update_msg = status_respuesta_json["services"][0]["incidents"][0]["updates"][0]["content"]
    return update_msg
