import os

import discord
from dotenv import load_dotenv
from processfuncs import *
from keras import models
import pickle
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

comment_model = models.load_model('comment_class_model.h5')


@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)

    
    print(f'{client.user} has connected to guild: {guild.name}, id = {guild.id}!')



@client.event
async def on_message(message):
    
    if message.author == client.user:
        return
    
    toxic_flag = is_toxic(message.content, comment_model, tokenizer) 
    channel_id = message.channel.id
    channel = client.get_channel(channel_id)
    
    if toxic_flag:
        

        await channel.send(f"{message.author.mention()}, let's be nice and respectful here!")
   

client.run(TOKEN)
    

