import random
import requests
import math
from time import sleep as eep
from bot_logic import gen_pass,coinflip
import discord
from discord.ext import commands
import os
intents = discord.Intents.default()
intents.message_content=True
intents.message_content = True

bot = commands.Bot(command_prefix="yu!",intents=intents)

def getthing():
    res = requests.get('https://random-d.uk/api/random')
    data = res.json()
    return data["url"]
@bot.event
async def on_ready():
    1==1


@bot.command()
async def hello(ctx):
    await ctx.send("yo")

@bot.command()
async def meme(ctx,me):
    try:
        with open(f"images/{me}","rb") as f:
            await ctx.send(file=discord.File(f))
    except:
        if me=="random":
            with open(f"images/{random.choice(os.listdir('images'))}","rb") as f:
                await ctx.send(file=discord.File(f))
        elif me=="list":
            d=""
            for i in os.listdir("images"):
                d+=i+"\n"
            await ctx.send(d,delete_after=5)
        else:
            await ctx.send("nah twin we don`t have that shi")
    await ctx.message.delete()

@bot.command()
async def dica(ctx):
    tot=[]
    with open("tips.txt","r",encoding="utf-8") as f:
        for d in f:
            tot.append(d.strip())
    await ctx.send(random.choice(tot))

@bot.command()
async def fetchme(ctx,im):
    await ctx.send(getthing())

@bot.command()
async def ruisend(ctx):
    mes=""
    for i in range(len("yu!ruisend "),len(str(ctx.message.content))):
        mes+=str(ctx.message.content)[i]
    await ctx.message.delete()
    await ctx.send(mes)

@bot.command()
async def coin(ctx):
    await ctx.send(coinflip())


@bot.command()
async def secret(ctx):
    await ctx.send(gen_pass(random.randint(10,30)),delete_after=.5)

@bot.command()
async def add(ctx, left, right):
    try:
        await ctx.send(int(left) + int(right))
    except:
        await ctx.send("uhh..")

bot.run("token")
