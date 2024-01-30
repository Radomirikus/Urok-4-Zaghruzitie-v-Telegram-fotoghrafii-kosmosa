import telegram

bot = telegram.Bot(token='6941078604:AAG0j6LkKrcbp4WNvJ-TmPk_fileOikl--Q')
print(bot.get_me())
bot.send_message(chat_id='@spaceimagesultra', text="""I put the new Forgis on the Jeep
I trap until the bloody bottoms is underneath
'Cause all my niggas got it out the streets
I keep a hundred racks inside my jeans
I remember hittin' the mall with the whole team
Now a nigga can't answer calls 'cause I'm ballin'
I was wakin' up, gettin' racks in the morning
I was broke, now I'm rich, these niggas salty""")

bot.send_document(chat_id='@spaceimagesultra', document=open('images/nasa_planet_image_0.png', 'rb'))