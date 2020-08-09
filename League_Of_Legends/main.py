import requests
import json
import Data_Servers, status_server

try:  
    print('¡SALUDOS INVOCADOR!')
    apikey = {
        'api_key': ''
        }
    
    def info_avanzada(id_summoner, servidor_lol):
        info_avanzada_summoner = requests.get("https://{}.api.riotgames.com/lol/league/v4/entries/by-summoner/{}".format(servidor_lol, id_summoner), params=apikey) #Petición API Riot Games
        status_respuesta_avanzada = info_avanzada_summoner.status_code   #Línea de código para sacar HTTP STATUS CODE
        if status_respuesta_avanzada == 200:  # STATUS CODE de request accepted   
            info_avanzada_summoner_list = info_avanzada_summoner.json()
            if  info_avanzada_summoner_list != []:
                league_points = info_avanzada_summoner_list[0]["leaguePoints"]
                tier_rank = info_avanzada_summoner_list[0]["tier"] + "," + info_avanzada_summoner_list[0]["rank"]
                wins = info_avanzada_summoner_list[0]["wins"]
                losses = info_avanzada_summoner_list[0]["losses"]
                winrate = wins/(wins + losses) * 100
                hotstreak = info_avanzada_summoner_list[0]["hotStreak"]
                print('INFORMACIÓN AVANZADA.... \n')
                print(f'El invocador actualmente está en el elo: {tier_rank} con {league_points}pl')
                print(f'Tiene {wins} victorias y {losses} derrotas, su winrate es de: {winrate}')
                if hotstreak == False:
                    print('Es la hora sad, invocador. No estás en racha de victorias!')
                else:
                    print('Majestuoso, invocador! Cuentas con racha de victorias')
                menu(servidor_lol)
            else:
                print('No se encontró experiencia en Rankeds')
                menu(servidor_lol)
            
            
        else:
            raise ConnectionError
    def info_basica():
        summoner_name = input('Ingrese su nombre de invocador: ')
        print('Servidores disponibles: ')
        Data_Servers._servers()
        servidor_lol = input('Ingrese el servidor en el que juega: ')
        
        if servidor_lol in Data_Servers.servers:
            info_basica_summoner = requests.get("https://{}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}".format(servidor_lol,summoner_name), params=apikey)  #Petición API Riot Games
            status_respuesta = info_basica_summoner.status_code #Línea de código para sacar HTTP STATUS CODE
            if status_respuesta == 200: #STATUS CODE de request accepted
                info_invocador = info_basica_summoner.json()  # Guardar datos del api como JSON
                nombre_invocador = info_invocador["name"]
                id_invocador = info_invocador["id"]
                lvl_invocador = info_invocador["summonerLevel"]
                id_img_invocador = info_invocador["profileIconId"]
                print("Nombre invocador: " + nombre_invocador)
                print(f'Nivel invocador: {lvl_invocador}')
                info_avanzada(id_invocador,servidor_lol)
            else:
                raise ConnectionError
        else:
            print('Servidor incorrecto')
            info_basica()
    def Consultar_Update(game_region):
        server = game_region
        print(status_server.Mensajes_RIOT(game_region))
        Decision_usuario = input("Digite 1 si desea salir del programa, 2 si desea consultar otro nombre de invocador: ")
        if Decision_usuario == '1':
            raise ConnectionAbortedError
        elif Decision_usuario == '2':
            info_basica()
        else:
            print("Opción invalida")
            menu(server)
            

    def menu(game_region):
        SERVER = game_region
        Decision_usuario = input("Digite 0 si desea consultar las últimas noticias, 1 si desea salir del programa, 2 si desea consultar otro nombre de invocador: ")
        if Decision_usuario == '0':
            Consultar_Update(game_region)
        elif Decision_usuario == '1':
            raise ConnectionAbortedError
        elif Decision_usuario == '2':
            info_basica()
        else:
                print("Opción invalida")
                menu(SERVER) 
                
    if __name__ == "__main__":
        info_basica()
            

        
except ConnectionAbortedError:
    print('Fin programa')
except ConnectionRefusedError:
    print('Servidor no disponible')
except ConnectionError:
    print('Error en la conexión al API')
except:
    print('Unknown error')


