# ------------------------------------------------------------------------СПАРАВКА О ПРОБЛЕМЕ------------------------------------------------------------------------------------------------------------------------------------
# при выводе (в строках 23-25) получаю значение None, такое происходит при любых изменениях
# в папке CB_rf был изменен код, посмотрить его, вроде бы он правельный
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
from CB_rf import get_course
from wiki import get_article

token = "vk1.a.-kZYAYNQphUbnUdeIrHbGuwSV6N2aFeyaDsIGaumDerGzq9N9KimTQWR0L8B_pc5ai71BCGNyTRlijK3h8u0BP5o4s9j-Mc6bFAGHzg0GKLfgrgDi1PfwwumiwGDiOiOHG6qCw_8Ag6-IPp38eVYb8VNHzefFUkwGtQib5KpHN4tHmQpe9-1tv-gVPcoxJSSn9QsLPn-rbyIRZDuyKlhPg"\

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        msg = event.text.lower()
        random_id = random.randint(-10 ** 7, 10 ** 7)
        user_id = event.user_id
        if msg[:2] == "-к":
            article1 = msg[2:].strip()
            response = str(get_course(article1))
        elif msg[:2] == "-в":
            article = msg[2:]
            response = get_article(article)
        elif msg[:2] == "-с":
            response = "Вот ссылка на YOUTUBE - {0}\n Вот ссылка на VK - {1}\n Вот ссылка на INSTOGRAM - {2} ".format(
                "https://www.youtube.com/",
                "https://vk.com/feed", 
                "http://instagram.com/"
                )
        else:
            response = "Не знаю"
        vk.messages.send(
            user_id=user_id,
            random_id=random_id,
            message=response,
        )






# R01239
# R01375
