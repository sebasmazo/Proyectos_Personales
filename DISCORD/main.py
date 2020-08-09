import discord
import numpy.random as rnd
import requests

TOKEN = ''
PARAMS = {'api_key': 'g6oYHeAoWn8uqW8EGRMSi9VpbSTwQOcy'}
client = discord.Client()
    #GIPHY
commands = " $amame: Te dice te amo \n $algo: Dice un dato curioso bro \n $hello: Te saluda equisde \n $gif: Busca un gif aleatorio "
mensajes_curiosos = ['Hola soy santos', 'Parangacutirimicuara', 'Sabias que el cuello de los pinguinos es más largo que el torso', 'Mazo es mi dios', 'Dame daneeeee', 'Miguel rico', 'Arroz con leche me quiero casar', 'Mi pan, susususm, sususususm']
stonks = 0
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send(f'Hello, {message.author}!')
    
    if message.content.startswith('$algo'):
        index = rnd.randint(0, len(mensajes_curiosos))
        await message.channel.send(mensajes_curiosos[index])
    
    if message.content.startswith('$amame'):
        await message.channel.send(f'Te amo, {message.author}')
    
    if message.content.startswith('$gif'):
        r = requests.get(url='http://api.giphy.com/v1/gifs/random', params=PARAMS)
        data = r.json()
        await message.channel.send('Tu gif mi lord: {}' .format(data["data"]["images"]["downsized_large"]["url"]))

    if message.content.startswith('$comandos'):
        await message.channel.send(commands)
    
    if message.content.startswith('$stonks'):
        stonks =+ 1
        await message.channel.send(str(stonks))
    
    

    
client.run(TOKEN)
