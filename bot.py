import os

import discord
from dotenv import load_dotenv
#from processfuncs import *
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)

    
    print(f'{client.user} has connected to guild: {guild.name}, id = {guild.id}!')



@client.event
async def on_message(message):
    
    if message.author == client.user:
        return
    
    print(f'{message.author}: {message.content}')


client.run(TOKEN)
    

