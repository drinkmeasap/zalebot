import discord
import asyncio
from tokenbot import token
from time import sleep
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!hello'):
        await client.send_message(message.channel,  'Hello ' + str(message.author))
        

        
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

client.run(token)