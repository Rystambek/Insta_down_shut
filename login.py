from instagrapi import Client

USERNAME = "rystambek_809"
PASSWORD = "Rustambek20"

cl = Client()
cl.login(USERNAME, PASSWORD)
cl.dump_settings("session.json")  # Sessiyani saqlab qo'yish
print("Login muvaffaqiyatli bajarildi!")
