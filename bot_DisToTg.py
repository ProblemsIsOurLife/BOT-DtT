import discord
import config
import requests
import io

captured_message = ''
file = io.BytesIO()
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        channel = self.get_channel(config.DiscordChannelID)
        if message.channel == channel:
            captured_message = 'Message from {0.author}:\n{0.content}'.format(message)
            print('Message from {0.author}: {0.content}'.format(message))
            if message.author == client.user:
                return
        #await message.channel.send(captured_message)
        if not message.attachments:
            TGBot.send_mess(captured_message)
        if message.attachments:
            print('Message from {0.author}: image'.format(message))
            TGBot.send_mess(captured_message)
            for attach in message.attachments:
                await attach.save(file, seek_begin=True, use_cached=False)
                TGBot.send_file(file)
                file.truncate(0)

class TGBot:
    def send_mess( text):  
        params = {'chat_id': config.TGchatID, 'text': text}
        response = requests.post(config.url + 'sendMessage', data=params)
        return response
    def send_file(file):
         params = {'chat_id': config.TGchatID}
         file ={'photo': file.getvalue()} 
         response = requests.post(config.url + 'sendPhoto', data=params,files=file)
         return response
client = MyClient()
client.run(config.DiscordToken)
