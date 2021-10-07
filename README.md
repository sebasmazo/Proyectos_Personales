ENGLISH ----#---- Documentation
# Personal_Projects
 Projects carried out with the intention of practicing and gaining knowledge in the languages developed
 
 Project #1 League Of Legends
 {
 
   Small project using the Riot Games API to consult player statistics and consult news made by rioters, application developed for a console environment

   Developer: Sebastián Mazo Vélez 
   Languages used: Python 
   Imported Libraries: JSON, Requests
   Development Time: 6 Hours 
   Developer language appropriation: Medium
   Open Source, suggestions are accepted and can be used freely
   
   Documentation:
   	functions {
		info_basic() // Main function, it takes care of taking the user's input and distributing this input through the different functions, it makes the first connection to the api to take basic data from the caller such as name, level, id, icon id, etc. When finished, it directs to info_avanced sending the id and the server as parameter
		advanced_info(id_summoner,server_lol) //Function in charge of collecting more complex data from api, Wins, losses, elo, winrate and hotstreak. When finished, it leads to the menu function with the server as parameter.
		menu(game_region) // This function is simply a menu made with if and elif, the user can choose to consult another user, exit the program or consult updates made by the rioters (Game news)
		Consult_Update(game_region) // This function shows the user through a query to the api the latest updates made by rioters (News)
	}
	external functions imported from other .py documents {
		Imported documents: Data_Servers.py, status_server.py
		Data_Servers {
			In this document you can find the list of servers enabled to consult in the form of DICT and a function to print the keys, we use this function when we show the user the servers available to choose
		}
		status_server {
			In this document there are two functions (check_status && Mensajes_RIOT), check_status checks if the league of legends server is online and Mensajes_RIOT takes care of getting the latest messages, updates, news made by the rioters we use this function in the main when we do Consult_Update()
		}
	
	
}

# Proyectos_Personales
 Proyectos realizados con intención de prácticar y ganar conocimiento en los lenguajes desarrollados
 
 Proyecto #1 League Of Legends
 {
 
   Pequeño proyecto usando la API de Riot Games para consultar estadisticas de jugador y consultar noticias hechas por rioters, aplicación desarrollada para un entorno en consola

   Desarrollador: Sebastián Mazo Vélez 
   Lenguajes Utilizados: Python 
   Librerias Importadas: JSON, Requests
   Tiempo Desarrollo: 6 Horas 
   Apropiación de lenguaje por parte del desarrollador: Mediano
   Open Source, se aceptan sugerencias y se puede utilizar libremente
   
   Documentación:
   	funciones {
		info_basica()	//Función principal, se encarga de tomar el input del usuario y repartir este input por las distintas funciones, hace la primera conexión a la api para 						tomar datos basicos del invocador como nombre, level, id, icon id, etc. Al terminar dirige a info_avanzada mandando el id y el servidor como parametro
		info_avanzada(id_summoner,servidor_lol)	//Función encargada de recopilar datos más complejos de la api, Wins, losses, elo, winrate y hotstreak. Al terminar, dirige a la 												   función de menu con el servidor como parametro.
		menu(game_region)	//Esta función es simplemente un menu hecho con if y elif, el usuario podrá elegir entre consultar otro usuario, salir del programa o consultar 								  actualizaciones hechas por los rioters (Noticias del juego)
		Consultar_Update(game_region)	//Esta función se encarga de mostrar al usuario por medio de un query a la api las ultimas actualizaciones hechas por rioters (Noticias)
	}
	funciones externas importadas desde otros documentos.py {
		Documentos importados: Data_Servers.py, status_server.py
		Data_Servers {
			En este documento se encuentra la lista de servers habilitados para consultar en forma de DICT y una función para imprimir las keys, recurrimos a esta función cuando 			  le mostramos al usuario los servers disponibles para elegir
		}
		status_server {
			En este documento hay dos funciones (verificar_status && Mensajes_RIOT), verificar status revisa si el server de league of legends está online y Mensajes_RIOT se 	             encarga de sacar los ultimos mensajes, actualizaciones, noticias hechas por los rioters recurrimos a esta función en el main cuando hacemos Consultar_Update()
		}
	
	
}




			
 

 
