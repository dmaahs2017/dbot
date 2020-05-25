#!/usr/bin/python3
import discord
from discord.ext import commands
import parser
from cogs.actions import Actions

# SETUP

CLIENTID = 710029944646008883
PERMISSIONINT = 67584
print(discord.__version__)
print("This invite link for your bot is: " +
      f"https://discordapp.com/oauth2/authorize?client_id={CLIENTID}&scope=bot&permissions={PERMISSIONINT}")
token = open("../res/token.txt", "r").read()

bot = commands.Bot(command_prefix='dbot.')


@bot.event
async def on_ready():
    print(f'We have loggin in as {bot.user}')

# ADD COGS
bot.add_cog(Actions(bot))

# START BOT
bot.run(token)
