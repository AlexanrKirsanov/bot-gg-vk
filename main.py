import os
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from dotenv import load_dotenv

load_dotenv()

VK_TOKEN = os.getenv("VK_TOKEN")

def send_message(vk, user_id, message):
    vk.messages.send(user_id=user_id, message=message, random_id=0)

def main():
    if not VK_TOKEN:
        print("Ошибка: VK_TOKEN не найден. Укажите токен в переменных окружения.")
        return

    try:
        vk_session = vk_api.VkApi(token=VK_TOKEN)
        vk = vk_session.get_api()
        longpoll = VkLongPoll(vk_session)
        print("Бот Глобального Гносиса запущен...")

        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                user_id = event.user_id
                text = event.text.lower().strip()

                if text in ["привет", "начать", "start", "hello"]:
                    with open("hello.info", encoding="utf-8") as f:
                        greeting = f.read()
                    send_message(vk, user_id, greeting)
                else:
                    send_message(vk, user_id, "Ваше сообщение получено. Бот в стадии разработки.")

    except Exception as e:
        print(f"Ошибка при запуске бота: {e}")

if __name__ == "__main__":
    main()
