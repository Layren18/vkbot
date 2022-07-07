import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from config import token

vk_session = vk_api.VkApi(token = '5a463519111fa39a271401b0b2ecb7345470d21727d02c9c5556eafbffa7d2961caafa44f43b22968d592')
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

def sender(id, text):
	vk.messages.send(user_id = id, message = text, random_id = 0)

def send_stick(id, number):
	vk.messages.send(user_id = id, sticker_id = number, random_id = 0)

for event in longpoll.listen():
	if event.type == VkEventType.MESSAGE_NEW:
		if event.to_me:

			msg = event.text.lower()
			id = event.user_id

			if msg == 'привет':
				sender (id, 'И тебе привет!')
				send_stick(id, 20525)