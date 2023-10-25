import os
from random import choice
from colorama import *
from colorama import Fore
from langs import RU, ENG
from pyrogram import Client
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import ApiIdInvalid
from pyrogram.errors.exceptions.not_acceptable_406 import PhoneNumberInvalid

def banner():
    print(Fore.MAGENTA+'''
▒█░░░ █▀▀█ █▀▄▀█ █▀▀▄ █▀▀▄ █▀▀█ ▒█▀▀▀█ ▀▀█▀▀ █▀▀ █▀▀█ █░░ 
▒█░░░ █▄▄█ █░▀░█ █▀▀▄ █░░█ █▄▄█ ░▀▀▀▄▄ ░░█░░ █▀▀ █▄▄█ █░░ 
▒█▄▄█ ▀░░▀ ▀░░░▀ ▀▀▀░ ▀▀▀░ ▀░░▀ ▒█▄▄▄█ ░░▀░░ ▀▀▀ ▀░░▀ ▀▀▀
          

                        by https://t.me/CEKCYAJIHbIU
                        channel: https://t.me/lambdaHEHE
          
    ~stop script by pressing Ctrl+C~\n\n''')

def get_api() -> list():
    cfg = open('cfg.txt', 'w+')
    settings = []
    lang_i = input(Fore.MAGENTA+'Choose your language (RU or ENG):')
    while True:
        if lang_i.lower() not in ('ru', 'eng'):
            lang_i = input(Fore.MAGENTA+'You enter wrong data, try again (RU or ENG):')
        else:
            lang = 'ru' if lang_i.lower() == 'ru' else 'eng'
            settings.append(lang)
            break
    try:
        api_id = int(input(RU['api_id_input'] if lang == 'ru' else ENG['api_id_input']))
    except:
        print(RU['error_api'] if lang == 'ru' else ENG['error_api'])
    api_hash = input(RU['api_hash_input'] if lang == 'ru' else ENG['api_hash_input'])
    settings.extend((str(api_id), api_hash))
    print(RU['success_api'] if lang == 'ru' else ENG['success_api'])
    while True:
        phone = input(RU['phone_input'] if lang == 'ru' else ENG['phone_input'])
        try:
            app = Client(name='LambdaSteal', api_id=settings[1], api_hash=settings[2])
            app.DEVICE_MODEL = 'Lambda_Crypto_Stealer'
            app.connect()
            sent_code_info = app.send_code(phone)
            while True:
                try:
                    code = input(RU['code_input'] if lang == 'ru' else ENG['code_input'])
                    app.sign_in(phone, sent_code_info.phone_code_hash, code)
                    print(RU['code_success'] if lang == 'ru' else ENG['code_success'])
                    break
                except:
                    print(RU['code_error'] if lang == 'ru' else ENG['code_error'])
            app.disconnect()
            break
        except PhoneNumberInvalid:
            print(RU['phone_error'] if lang == 'ru' else ENG['phone_error'])
    try:
        app.disconnect()
    except:
        pass
    cfg.write(';'.join(settings))
    cfg.close()
    return settings
