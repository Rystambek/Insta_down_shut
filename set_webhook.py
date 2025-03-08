import requests
import os

url = 'https://instadownloderbot.pythonanywhere.com/webhook'

Token = '7604363956:AAH9UwqqZ-1SBuIzTJeur_lQiCh6rJOJ2tY'

payload = {
    "url":url
}

r = requests.get(f"https://api.telegram.org/bot{Token}/setWebhook", params=payload)
r = requests.get(f"https://api.telegram.org/bot{Token}/GetWebhookInfo", params=payload)



print(r.json())