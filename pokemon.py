import json
import os
from random import randrange, randint
from urllib.request import Request, urlopen
import vk_api
from vk_api.longpoll import VkEventType, VkLongPoll

TOKEN = "vk1.a.CHziGOs1cf-sjGndCHAOrRRBcFmp25X7l3SAlM-QUNvPmbAmeCX3Nif_iua5L00h4Vc9BoBdB_EJjk9YKmiTTNvBdCFqMF1rgTeqJ8L_j5iZPI_SgqFJP1e022j2J-e8V5qVJWXLJl6AyHLD92IB0UAGUX6M4kso3OGi1yPB8OFA3_QT4Pu9QTtMqUk5CjeiZIfKAwmy6a5kn-PDd2To5g"
vk_sesion = vk_api.VkApi(token=TOKEN)
longpoll = VkLongPoll(vk_sesion)
vk = vk_sesion.get_api()

req = Request("https://pokeapi.co/api/v2/pokemon", headers = {'User-Agent': 'Mozila/5.0'})
response = urlopen(req)
count = json.loads(response.read())['count']

req = Request(f"https://pokeapi.co/api/v2/pokemon/?limit{count}", headers = {'User-Agent': 'Mozila/5.0'})
response = urlopen(req)
pokemons = json.loads(response.read())['results']
print(pokemons)
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        if event.from_user:
            for pokemon in pokemons:
                if pokemon['name'] == event. text:
                    req = Request(pokemon["url"], headers = {'User-Agent': 'Mozila/5.0'})
                    response = urlopen(req)
                    desc = json.loads(response.read())
                    message = f"Имя: {desc['name']}\nРост: {desc['height']}\nBec: {desc['weight']}"
                    vk.messages.send(user_id=event.user_id, message=message, random_id=randint(1, 10000))
                    break
