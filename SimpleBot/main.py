import os
import discord
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('key1')
client = discord.Client(intents=discord.Intents.default())

Something = "Hi, I am Simple Bot, I do Simple things"

def Game():
  sum = random.randint(1,1000)
  return sum

@client.event
async def on_message(msg):
  if msg.author == client.user:
    return 
  if msg.content.startswith("roll"):  
   await msg.channel.send(Game())
    
  if msg.content.startswith("say hi"):  
   await msg.channel.send(Something) 
    
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)