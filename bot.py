import telebot
import instaloader
import os

TOKEN = "5464450219:AAFXSLhDKPgK-mnvkpSXSacm1zMi3JckcVE"
bot = telebot.TeleBot(TOKEN)


L = instaloader.Instaloader()

@bot.message_handler(commands=['start'])
def start(message):
    name = message.from_user.first_name
    bot.reply_to(message,f"مرحبا بك ({name}) في بوت التحميل من الانستقرام")


def extract_reel_id(url):
    try:
        return url.split("/reel/")[1].split("/")[0]
    except IndexError:
        return None


@bot.message_handler(func=lambda message: "instagram.com/reel/" in message.text)
def download_reel(message):
    url = message.text
    reel_id = extract_reel_id(url)

    if not reel_id:
        bot.reply_to(message, "❌ رابط غير صالح، يرجى إرسال رابط صحيح لـ Reels.")
        return

    bot.reply_to(message, "⏳ جاري تحميل الريلز، انتظر لحظات...")

    try:
        post = instaloader.Post.from_shortcode(L.context, reel_id)
        L.download_post(post, target="reels")

        for file in os.listdir("reels"):
            if file.endswith(".mp4"):
                video_path = os.path.join("reels", file)
                
                
                with open(video_path, "rb") as video:
                    bot.send_video(message.chat.id, video)

                # delet video
                os.remove(video_path)
                os.rmdir("reels")
                break

    except Exception as e:
        bot.reply_to(message, f"")




# تشغيل البوت
bot.polling(none_stop=True)
