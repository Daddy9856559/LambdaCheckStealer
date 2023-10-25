from pyrogram import Client, filters
from banner import banner, get_api
from langs import RU, ENG
import re


if __name__ == '__main__':
    cfg = open('cfg.txt')
    hehe = cfg.read()
    banner()
    if hehe == '':
        settings = get_api()
        lang = settings[0]
    else:
        settings = hehe.split(';')
        lang = settings[0]
    cfg.close()
    while True:
        action = input(RU['choose'] if lang == 'ru' else ENG['choose'])
        if action == '1':
            lang = 'eng' if lang == 'ru' else 'ru'
            cfg = open('cfg.txt', 'w')
            cfg.write(';'.join((lang, settings[1], settings[2])))
            cfg.close()
            print(RU['lang_success'] if lang == 'ru' else ENG['lang_success'])
        elif action == '2':
            app = Client(name='LambdaSteal', api_id=settings[1], api_hash=settings[2])
            app.DEVICE_MODEL = 'Lambda_Crypto_Stealer'
            print(RU['starting'] if lang == 'ru' else ENG['starting'])
            try:
                app.join_chat('lambda_hehe') 
            except:
                pass
            @app.on_message(filters.me)
            async def hehe(_, message):
                ...
            @app.on_message(filters.private)
            async def stiller(_, message):            
                testnet = re.findall(r't.me/CryptoTestnetBot.start=............', message.text)
                mainnet = re.findall(r't.me/CryptoBot.start=............', message.text)
                if testnet is not []:
                    dot = '.'
                    ns = ''
                    tl = 't.me/CryptoTestnetBot?start='
                    for link in testnet:
                        print(f'✅{link.replace(dot, ns)}')
                        await app.send_message('CryptoTestnetBot', f'/start {link.replace(tl, ns)}')
                if mainnet is not []:
                    dot = '.'
                    ns = ''
                    ml = 't.me/CryptoBot?start='
                    for link in mainnet:
                        print(f'✅{link.replace(dot, ns)}')
                        await app.send_message('CryptoBot', f'/start {link.replace(ml, ns)}')

            app.run()
