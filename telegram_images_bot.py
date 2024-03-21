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
    chanell_name = os.getenv("TG_CHAT_ID")

    parser = argparse.ArgumentParser(description='отправляет в тг канал снимки nasa и SpaсeX')
    parser.add_argument('--cooldown', help='укажите задержку в отправке фотографий', default=14400)
    args = parser.parse_args()
    delay = 2

    while True:
        directory_object = os.walk('images')
        for elements in directory_object:
            folder, nested_folder, files = elements
            random.shuffle(files)
            for image in files:
                with open(f'images/{image}', 'rb') as file:
                    bot.send_document(chat_id=chanell_name, document=file)
                    time.sleep(delay)
        time.sleep(args.cooldown)

if __name__ == "__main__":
    main()