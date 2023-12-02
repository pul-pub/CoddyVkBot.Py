import vk_api
from random import randint, choice
from vk_api.longpoll import VkLongPoll, VkEventType

TOKEN = "TOKEN"
vkSession = vk_api.VkApi(token=TOKEN)
longpoll = VkLongPoll(vkSession)
vk = vkSession.get_api()

vars = ["камень", "ножницы", "бумага"]
out = None
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text.lower() in vars:
        if event.from_user:
            user = event.text.lower()
            bot = choice(vars)
            vk.messages.send(user_id = event.user_id, message = bot, random_id = randint(1, 10000))
            ont = None
            if bot == 'камень':
                if user == 'камень':
                    out = 'Ничья'
                elif user == 'ножницы':
                    out = 'Ты проиграл'
                else:
                    out = 'Ты выиграл'
            elif bot == 'ножницы':
                if user == 'камень':
                    out = 'Ты выиграл'
                elif user == 'ножницы':
                    out = 'Ничья'
                else:
                    out = 'Ты проиграл'
            else:
                if user == 'камень':
                    out = 'Ты проиграл'
                elif user == 'ножницы':
                    out = 'Ты выиграл'
                else:
                    out = 'Ничья!'
            vk.messages.send(user_id=event.user_id, message=out, random_id=randint(1, 10000))
