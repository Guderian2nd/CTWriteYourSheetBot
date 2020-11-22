# bot.py
import os
import random
from dotenv import load_dotenv

# 1
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# 2
bot = commands.Bot(command_prefix='=')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.author.discriminator == '2163':
        response = ':CTSheet:'
        await message.channel.send(response)

    await bot.process_commands(message)

@bot.command(name='CT')
async def show_ct_sheet(ctx):
    response = 'CT write the damn sheet :page_facing_up:'
    await ctx.send(response)

bot.run(TOKEN)