import os
from random import randrange, randint
from urllib.request import Request, urlopen
import json
import vk_api
from vk_api.longpoll import VkEventType, VkLongPoll
from youtubesearchpython import VideosSearch

TOKEN = "-----------------------------TOKEN-------------------------------------"
vk_sesion = vk_api.VkApi(token=TOKEN)
longpoll = VkLongPoll(vk_sesion)
vk = vk_sesion.get_api()

def GetPocemons():
    _req = Request("https://pokeapi.co/api/v2/pokemon", headers = {'User-Agent': 'Mozila/5.0'})
    _response = urlopen(_req)
    _count = json.loads(_response.read())['count']

    _req = Request(f"https://pokeapi.co/api/v2/pokemon/?limit{_count}", headers = {'User-Agent': 'Mozila/5.0'})
    _response = urlopen(_req)
    _pokemons = json.loads(_response.read())["results"]
    return _pokemons

def FindPokemon(_pokemons, _name):
    for _pokemon in _pokemons:
        if _pokemon['name'] == _name:
            _req = Request(_pokemon["url"], headers={'User-Agent': 'Mozila/5.0'})
            _response = urlopen(_req)
            _desc = json.loads(_response.read())
            _message = f"Имя: {_desc['name']}\nРост: {_desc['height']}\nBec: {_desc['weight']}"
            return _message

def FindVideos(_name):
    link = VideosSearch(_name, limit=1).result()["result"][0]["link"]
    return link

pokemons = GetPocemons();

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        if event.from_user:
            command = event.text.split(" ")[0].lower();
            name = event.text.split(" ")[1].lower();
            if command == "/pokemon":
                massage = FindPokemon(pokemons, name)
                print(vk.messages.send(user_id=event.user_id, message=massage, random_id=randint(1, 10000)))
            elif command == "/youtube":
                massage = FindVideos(name)
                print(vk.messages.send(user_id=event.user_id, message=massage, random_id=randint(1, 10000)))

