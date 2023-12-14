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

client.run('NzA1MzEyOTQwODMxODAxMzQ1.GRomKg.S4m3j-MsSE8E20FKFNd4up4-AotcQG8JV6-Xq0')
