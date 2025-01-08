import discord
from scrapper import Scrapper

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def build_message(item):
    embed = discord.Embed(type="rich", title=item["name"])
    embed.set_thumbnail(url=item["image"])
    embed.url = item["url"]
    embed.add_field(name="가격", value=item["price"], inline=True)
    return embed

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('안녕!'):
        await message.channel.send('Hello!')

    if message.content.startswith("!노트북"):
        scrapper = Scrapper()
        results = scrapper.do()

        embeds = []
        for item in results:
            embeds.append(build_message(item))

        await message.channel.send(embeds=embeds)

client.run('YOUR TOKEN')