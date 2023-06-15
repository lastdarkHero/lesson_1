import vk_api
import random
from Cb_rf import get_dollor_course

token = "vk1.a.-kZYAYNQphUbnUdeIrHbGuwSV6N2aFeyaDsIGaumDerGzq9N9KimTQWR0L8B_pc5ai71BCGNyTRlijK3h8u0BP5o4s9j-Mc6bFAGHzg0GKLfgrgDi1PfwwumiwGDiOiOHG6qCw_8Ag6-IPp38eVYb8VNHzefFUkwGtQib5KpHN4tHmQpe9-1tv-gVPcoxJSSn9QsLPn-rbyIRZDuyKlhPg"

vk = vk_api.VkApi(token=token)


while True:
 messages = vk.method("messages.getConversations", {"filter": "unanswered"})
 if messages["count"] > 0:
  user_message = messages["items"][0]["last_message"]["text"]
  user_id = messages["items"][0]["last_message"]["from_id"]

  if user_message.lower() == "папапеве курс":
   ans = f"Курс доллара на сегодня состовляет {get_dollor_course()} руб."
  else:
   ans = "Не знаю что это такое"

  vk.method(
    "messages.send", 
    {
        "random_id": random.randint(-10 ** 7, 10 ** 7),
        "message": ans,
        "user_id": user_id
    }
 )
