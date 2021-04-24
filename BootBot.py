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

        if message.content.lower().startswith('$stats'):
            counter_all = 0
            counter_author = 0
            async for m in message.channel.history(limit=50):
                if m.author != self.user and m.content.lower() == '$hello':
                    counter_all = counter_all + 1
                    if m.author == message.author:
                        counter_author = counter_author + 1

            await message.channel.send('There are ' + str(counter_all) + ' $hellos. ')
            await message.channel.send('You send ' + str(counter_author) + ' $hellos. ')


client = MyClient()
client.run(sys.argv[1])
