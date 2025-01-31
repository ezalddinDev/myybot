import requests
import telebot

bot = telebot.TeleBot("5464450219:AAFXSLhDKPgK-mnvkpSXSacm1zMi3JckcVE")


@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, f"اهلا بيك ({message.from_user.first_name}) في بوت التحميل من الانستكرام ارسل رابط الفديو ")

@bot.message_handler(commands=['id','ايدي'])
def id(message):
    name = message.from_user.first_name
    user = message.from_user.username
    di = message.from_user.id
    bio = bot.get_chat(message.from_user.id).bio
    bot.reply_to(message,f'NMAE>> {name}\nUSER>> @{user}\nID>> {di}\nBIO>> {bio}')

url = "https://instagram-scraper-2022.p.rapidapi.com/ig/post_info/"
@bot.message_handler(func= lambda m : True)
def reels(m):
    if "https://" in m.text:
        bot.reply_to(m,"Please wait for the video to load")
        sr = str(m.text).split("reel/")[1].split("/?")[0]
        querystring = {"shortcode": f'{sr}'}
        headers = {
	"X-RapidAPI-Key": "9dfd75e054msh243174963922ac0p167fd0jsn00a695f35ccb",
	"X-RapidAPI-Host": "instagram-scraper-2022.p.rapidapi.com"
}
        res = requests.request("GET", url, headers=headers, params=querystring)
        jso = res.json()
        iof = ''
    if "video_url" in jso:
        iof = jso['video_url']
        bot.send_video(m.chat.id,iof,)






bot.infinity_polling()
