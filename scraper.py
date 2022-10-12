from logging import error
from telethon import TelegramClient
from dotenv import load_dotenv
import os

# import time
# Load environment variables
load_dotenv()

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
api_name = os.getenv("API_NAME")

# Account Connection
client = TelegramClient(api_name, api_id, api_hash)


async def main():
    # Getting information about yourself
    me = await client.get_me()

    # "me" is a user object. You can pretty-print
    # any Telegram object with the "stringify" method:
    print(me.stringify())

    # When you print something, you see a representation of it.
    # You can access all attributes of Telegram objects with
    # the dot operator. For example, to get the username:
    # username = me.username
    # print(username)
    # print(me.phone)

    # You can print all the dialogs/conversations that you are part of:
    groups = []
    async for dialog in client.iter_dialogs():
        if str(dialog.id).startswith("-100"):

            groups.append(dialog.id)

            print(dialog.name, "has ID", dialog.id)
    with open("groups2.txt", "w") as f:
        for i in groups:
            f.write("{}\n".format(i))
            # print(i)
        f.close()

    print(f"{len(groups)} groups were detected!")
    # You can send messages to yourself...
    # await client.send_message('me', 'Hello, myself!')
    # ...to some chat ID

    # ...to your contacts
    # await client.send_message('+34600123123', 'Hello, friend!')
    # ...or even to any username
    # await client.send_message('username', 'Testing Telethon!')

    # You can reply to messages directly if you have a message object
    # await message.reply("Cool!")

    # Or send files, songs, documents, albums...
    # await client.send_file('me', '/home/me/Pictures/holidays.jpg')

    # You can print the message history of any chat:
    # async for message in client.iter_messages("me"):
    #     if message.id == 10480:
    #         with open("message.txt", "w", encoding="utf-8") as f:
    #             # print(message.text)
    #             f.write(str(message.text))
    # print(message.id, message.text)

    # You can download media from messages, too!
    # The method will return the path where the file was saved.
    # if message.photo:
    #     path = await message.download_media()
    #     print('File saved to', path)  # printed after download is done


with client:
    client.loop.run_until_complete(main())
