import discord
import parser
from random import randint

CLIENTID = 710029944646008883
PERMISSIONINT = 67584

print(discord.__version__)
print("This invite link for your bot is: " +
      f"https://discordapp.com/oauth2/authorize?client_id={CLIENTID}&scope=bot&permissions={PERMISSIONINT}")


token = open("token.txt", "r").read()

client = discord.Client()

def quote(person):
    quotes = open(person + "_quotes.txt").read()
    qs = []
    for q in filter(lambda l: "====================" != l, quotes.splitlines()):
        qs.append(q.replace('[', '').replace(']', '').replace("'", ''))

    return "> " + qs[randint(0, len(qs) - 1)] + '\n- ai-' + person
    
@client.event
async def on_ready():
    print(f'We have loggin in as {client.user}')

@client.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    botargs = message.content.lower().split(' ')
    if 'dbot.quote' == botargs[0]:
        if len(botargs) == 2:
            await message.channel.send(quote(botargs[1]))
        else:
            await message.channel.send(quote("joe"))
        

client.run(token)
