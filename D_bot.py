import discord
import parser
print(discord.__version__)

token = open("token.txt", "r").read()

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have loggin in as {client.user}')

@client.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")

    if parser.isCommand(message):
        await message.channel.send(parser.parse(message))


client.run(token)
