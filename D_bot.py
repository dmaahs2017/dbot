import discord
import parser
import os
import random

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

    return "> " + qs[random.randint(0, len(qs) - 1)] + '\n- ai-' + person

def instagram(acct):
    return f"instagram/{acct}/" + random.choice(os.listdir(f"instagram/{acct}/"))

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
    elif 'dbot.ig' == botargs[0]:
        await message.channel.send(f"Credit: ig@{botargs[1]}", file=discord.File(instagram(botargs[1])))
    elif 'dbot.ooo' == botargs[0]:
        await message.channel.send(":tophat:\n:eyes:\n:nose:\n:lips:")
    elif 'dbot.contribute' == botargs[0]:
        await message.channel.send("Consider Contributing to dbot at: https://github.com/dmaahs2017/discord-bots. Message @Dabrick2017#9824 for help :smiley:")
    elif 'dbot.help' == botargs[0] or 'dbot.h' == botargs[0]:
        await message.channel.send(
            "Commands:\n" +
            "\t`dbot.quote [person]` - generate a random quote from [person]\n" +
            "\t`dbot.ig {acct}` - generate a random ig post from ig@acct\n" +
            "\t`dbot.contribute` - see how you can contribute to this bot!\n" +
            "\t`dbot.h` or `dbot.help` - see this help list")
        

client.run(token)
