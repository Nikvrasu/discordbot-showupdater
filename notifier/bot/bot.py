import discord
from discord.ext import tasks

class Bot(discord.Client):
    def __init__(self, notifier):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)
        self.notifier = notifier

    async def on_ready(self):
        print(f'We have logged in as {self.user}')
        self.check_updates.start()

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('$hello'):
            await message.channel.send('Hello!')

    @tasks.loop(hours=2)
    async def check_updates(self):
        await self.notifier.check_for_updates(self)