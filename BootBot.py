import discord
import sys


class MyClient(discord.Client):
    async def on_ready(self):
        print('Beeeeep! Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author} contains {0.content}.'.format(message))
        if message.author == self.user:
            return

        if message.content.lower().startswith('$hello'):
            await message.channel.send('Hello!')
            await message.author.send('hello, how are you?')
        if message.content.lower().startswith('$stats'):
            counter = 0
            async for m in message.channel.history(limit=50):
                if m.author != self.user and m.content.lower() == '$hello':
                    counter = counter + 1
            await message.channel.send('There are ' + str(counter) + ' $hellos')


client = MyClient()
client.run(sys.argv[1])
