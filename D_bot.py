#!/usr/bin/python3
import discord
from discord.ext import commands
import parser
import os
import random

# SETUP

CLIENTID = 710029944646008883
PERMISSIONINT = 67584
print(discord.__version__)
print("This invite link for your bot is: " +
      f"https://discordapp.com/oauth2/authorize?client_id={CLIENTID}&scope=bot&permissions={PERMISSIONINT}")
token = open("token.txt", "r").read()

bot = commands.Bot(command_prefix='dbot.')


# HELPER FUNCTIONS


def __quote(person):
    quotes = open(person + "_quotes.txt").read()
    qs = []
    for q in filter(lambda l: "====================" != l, quotes.splitlines()):
        qs.append(q.replace('[', '').replace(']', '').replace("'", ''))
    return "> " + qs[random.randint(0, len(qs) - 1)] + '\n- ai-' + person


# BOT EVENT HANDLERS


@bot.event
async def on_ready():
    print(f'We have loggin in as {bot.user}')


@bot.command()
async def ig(ctx, acct):
    await ctx.send(f"Credit: ig@{acct}", file=discord.File(
        f"instagram/{acct}/" + random.choice(os.listdir(f"instagram/{acct}/"))
    ))


@bot.command()
async def quote(ctx, *persons):
    if len(persons) == 0:
        await ctx.send(__quote("joe"))
    else:
        await ctx.send(__quote(persons[0]))


@bot.command()
async def contribute(ctx):
    await ctx.send("Consider Contributing to dbot at: " +
                   "https://github.com/dmaahs2017/discord-bots. Message @Dabrick2017#9824 for help :smiley:")


@bot.command()
async def mood(ctx):
    await ctx.send(":tophat:\n:eyes:\n:nose:\n:lips:")

# START BOT
bot.run(token)
