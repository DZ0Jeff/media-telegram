from telethon import TelegramClient
from dotenv import load_dotenv
import os

load_dotenv()

api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')

bot_name = 'telework'

try:
    client = TelegramClient(bot_name, api_id, api_hash)
    client.start()
    print(f'[{bot_name}] Logado com sucesso!')

except Exception as error:
    print(f'[{bot_name}] Um erro aconteceu...')
    print(error)


async def main():
    print(f"[{bot_name}] A enviar arquivos...")
    await client.send_file("me", "Pearl Jam - 15 - Black.mp3")
    print(f"[{bot_name}] Finalizado!")


with client:
    client.loop.run_until_complete(main())