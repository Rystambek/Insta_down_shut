
import logging
import requests
import instaloader
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from instagrapi import Client

# Bot tokeni
TOKEN = "7604363956:AAH9UwqqZ-1SBuIzTJeur_lQiCh6rJOJ2tY"

# Instagram login
cl = Client()
cl.load_settings("session.json")  # Avval saqlangan sessiya orqali login qilish

# Logging sozlamalari
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

# Instagram yuklab olish funksiyasi
def download_instagram_video(url):
    L = instaloader.Instaloader()
    post = instaloader.Post.from_shortcode(L.context, url.split("/")[-2])
    return post.video_url

# Instagram'ga yuklash funksiyasi
def upload_to_instagram(video_path, caption=""):
    try:
        cl.video_upload(video_path, caption)
        return "Instagram'ga yuklandi!"
    except Exception as e:
        return f"Xatolik: {e}"

# /start komandasi
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Salom! Instagram video yuklab olish va yuklash uchun link yuboring.")

# Instagram video yuklab olish va yuklash
async def get_instagram_video(update: Update, context: CallbackContext):
    url = update.message.text
    if "instagram.com" in url:
        try:
            video_url = download_instagram_video(url)

            # Videoni yuklab olish
            video_path = "downloaded_video.mp4"
            with open(video_path, "wb") as f:
                f.write(requests.get(video_url).content)

            # Instagram'ga yuklash
            result = upload_to_instagram(video_path, "Bu avtomatik yuklangan video!")

            await update.message.reply_video(video_url)
            await update.message.reply_text(result)

        except Exception as e:
            await update.message.reply_text("Video yuklab bo�lmadi. Linkni tekshiring.")
    else:
        await update.message.reply_text("Iltimos, to�g�ri Instagram link yuboring.")

# Botni ishga tushirish
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, get_instagram_video))
    
    print("Bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()
