import telegram
import os
import random

bot = telegram.Bot(token='6941078604:AAG0j6LkKrcbp4WNvJ-TmPk_fileOikl--Q')
# for rickroll in range(1):
#     bot.send_message(chat_id='@spaceimagesultra', text="https://youtu.be/dQw4w9WgXcQ?si=4ZVhPJZQ3DMztKIh")
directory_object = os.walk('images')
for elements in directory_object:
    folder, nested_folder, files = elements
    random.shuffle(files)
    for image in files:
        bot.send_document(chat_id='@spaceimagesultra', document=open(f'images/{image}', 'rb'))