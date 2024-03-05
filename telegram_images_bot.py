import telegram
import os
import random
import time
import argparse
from dotenv import load_dotenv


def main():
    load_dotenv()
    telegram_token = os.getenv("TELEGRAM_TOKEN")
    bot = telegram.Bot(token=telegram_token)

    Chanell_name = os.getenv("CHAT_ID")
    bot.send_message(chat_id=Chanell_name, text="https://youtu.be/dQw4w9WgXcQ?si=4ZVhPJZQ3DMztKIh")

    parser = argparse.ArgumentParser(description='отправляет в тг канал снимки nasa и SpaсeX')
    parser.add_argument('cooldown', help='укажите задержку в отправке фотографий', default=14400)
    args = parser.parse_args()

    while True:
        directory_object = os.walk('images')
        for elements in directory_object:
            folder, nested_folder, files = elements
            random.shuffle(files)
            for image in files:
                image_extension = image.split(".")
                if len(image_extension) == 2:
                    bot.send_document(chat_id='@spaceimagesultra', document=open(f'images/{image}', 'rb'))
                    time.sleep(2)
        time.sleep(args.cooldown)


if __name__ == "__main__":
    main()