import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith('davi'):
            await message.channel.send('vai se fude <@200440751358738433>')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents, activity=discord.Game(name='Putaria'))

with open('path_to_your_file.txt', 'r') as file:
    file_contents = file.read()


client.run(file_contents)
