import os
from telethon import TelegramClient, events

api_id = int(os.environ.get('API_ID'))
api_hash = os.environ.get('API_HASH')
phone = os.environ.get('PHONE')

client = TelegramClient('session_bot', api_id, api_hash)




@client.on(events.NewMessage(chats=777000))
async def handlers(event):

    await client.forward_messages('me',event.message)


client.start()
client.run_until_disconnected()
