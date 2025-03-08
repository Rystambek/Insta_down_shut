import logging
import requests
import instaloader
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext, Dispatcher
from instagrapi import Client
import os
from bot import start,get_instagram_video,download_instagram_video,upload_to_instagram


TOKEN = "7604363956:AAH9UwqqZ-1SBuIzTJeur_lQiCh6rJOJ2tY"

bot = Bot(TOKEN)

app = Flask(__name__)

@app.route('/webhook', methods=["POST", "GET"])
def hello():
    if request.method == 'GET':
        return 'hi from Python2022I'
    elif request.method == "POST":
        data = request.get_json(force = True)
        
        dispacher: Dispatcher = Dispatcher(bot, None, workers=0)
        update:Update = Update.de_json(data, bot)
    
        #update 
        dispacher.add_handler(CommandHandler('start',start))
        dispacher.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, get_instagram_video))
         
        dispacher.process_update(update)
        return 'ok'

