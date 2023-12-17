import json
import  os
from  random import randrange
from urllib.request import Request, urlopen
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

TOKEN="vk1.a.CHziGOs1cf-sjGndCHAOrRRBcFmp25X7l3SAlM-QUNvPmbAmeCX3Nif_iua5L00h4Vc9BoBdB_EJjk9YKmiTTNvBdCFqMF1rgTeqJ8L_j5iZPI_SgqFJP1e022j2J-e8V5qVJWXLJl6AyHLD92IB0UAGUX6M4kso3OGi1yPB8OFA3_QT4Pu9QTtMqUk5CjeiZIfKAwmy6a5kn-PDd2To5g"
vkSession = vk_api.VkApi(token=TOKEN)
longpoll = VkLongPoll(vkSession)
vk = vkSession.get_api()

req = Request("https://pokeapi.co/api/v2/pokemon", headers = {'User-Agent': 'Mozila/5.0'})
response = urlopen(req)
count = json.loads(response.read())['count']

print(count)