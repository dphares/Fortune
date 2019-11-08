import discord
import asyncio
import os
import json
import random
import fortune

client = discord.Client()

try:  
   os.environ["discord_bot_token"]
except KeyError: 
   print ("Please set the environment variable discord_bot_token")
   sys.exit(1)

print(os.environ["discord_bot_token"])
secret_token = (os.environ["discord_bot_token"])
 
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
   channel = message.channel
   if message.content.startswith('!ping'):
      await channel.send( 'Pong!')
   if message.content.startswith('!ding'):
      await channel.send( 'Dong, motha fucka!')
   ### The magic
   if message.content.startswith('dicerolls'):
      msg = str(fortune.envselect())
      await channel.send(msg)

client.run(secret_token)