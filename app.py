import logging
import requests
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from instagrapi import Client
import os
from bot import start, get_instagram_video

# Bot tokeni
TOKEN = "7604363956:AAH9UwqqZ-1SBuIzTJeur_lQiCh6rJOJ2tY"
bot = Bot(TOKEN)

# Flask ilovasini yaratish
app = Flask(__name__)

# Telegram bot uchun Application
application = Application.builder().token(TOKEN).build()

# Webhook uchun route
@app.route('/webhook', methods=["POST", "GET"])
def webhook():
    if request.method == 'GET':
        return '✅ Flask Telegram bot ishlayapti!'

    elif request.method == "POST":
        data = request.get_json(force=True)
        update = Update.de_json(data, bot)

        # Telegram botga kelgan xabarlarni ishlash
        application.update_queue.put(update)
        
        return '✅ OK'

# Webhook o‘rnatish uchun route
@app.route('/set_webhook', methods=["GET"])
def set_webhook():
    WEBHOOK_URL = "https://yourdomain.com/webhook"  # O‘z domeningizni yozing
    success = bot.set_webhook(WEBHOOK_URL)
    return f"✅ Webhook o‘rnatildi: {success}"

# Flask serverni ishga tushirish
if __name__ == "__main__":
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, get_instagram_video))

    print("🚀 Flask server ishga tushdi...")
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
