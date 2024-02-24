import os
from random import randrange, randint
from urllib.request import Request, urlopen
import json
import vk_api
from vk_api.longpoll import VkEventType, VkLongPoll
from youtubesearchpython import VideosSearch
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
longpoll = VkLongPoll(vk_sesion)
vk = vk_sesion.get_api();

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        if event.from_user:
            link = VideosSearch()
        elif event.from_me:


