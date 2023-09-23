
import os
import discord
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


Something = "Hi, I am Simple Bot, I do Simple things"
meow = ['meow']
Cat_Gif = "https://tenor.com/view/cat-meow-fat-augh-gif-24948731"
Operator = ['+', '-', '*', "/"]
Stickman = "https://cdn.discordapp.com/attachments/1044692376746205244/1154472233805299743/59QL.gif"
WithoutMe = ['go', 'going','went','gonna']

def game():
  sum = random.randint(1,1000)
  return sum


def counter(msg):
  try:
    counter = int(msg.channel.last_message.content)
    counter += 1
    return counter
  except Exception as e:
    return "not a number" 

def calculator(msg):
  if('+' in msg):
    try:
      num = add(msg)
      return num
    except Exception as e:
      return "not number good"
  if('-' in msg):
    try:
      num = subtract(msg)
      return num
    except Exception as e:
      return "not number good"
  if('*' in msg):
    try:
      num = mutliply(msg)
      return num
    except Exception as e:
      return "not number good"
  if('/' in msg):
    try:
      num = divide(msg)
      return num
    except Exception as e:
      return "not number good"

def add(msg):
  try:
    first = float(msg[0:msg.index('+')])
    second = float(msg[msg.index('+') + 1: len(msg)])
    return first + second
  except Exception as e:
    return "not number in the message"

def subtract(msg):
  try:
    first = float(msg[0:msg.index('-')])
    second = float(msg[msg.index('-') + 1: len(msg)])
    return first - second
  except Exception as e:
    return "not number in the message"

def mutliply(msg):
  try:
    first = float(msg[0:msg.index('*')])
    second = float(msg[msg.index('*') + 1: len(msg)])
    return first * second
  except Exception as e:
    return "not number in the message"

def divide(msg):
  try:
    first = float(msg[0:msg.index('/')])
    second = float(msg[msg.index('/') + 1: len(msg)])
    return first / second
  except ZeroDivisionError as e:
    return "ur gonna create a blackhole"
  except ZeroDivisionError as e:
    return "not number in the message"
  
def meowSeparate(msg):
  return msg.replace("meow", "-meow-")

@client.event
async def on_message(msg):
  if msg.author == client.user:
    return 
  if msg.content.startswith("counter"):  
   await msg.channel.send(counter(msg))

  if any(word in msg.content for word in Operator): 
   await msg.channel.send(calculator(msg.content))

  if msg.content.startswith("roll"):  
   await msg.channel.send(game())
    
  if msg.content.startswith("say hi"):  
   await msg.channel.send(Something) 

  if msg.content.startswith("cat"):  
   await msg.channel.send(Cat_Gif) 

  if msg.content.startswith("stickman"):  
   await msg.channel.send(Stickman) 

  if any(word in msg.content for word in meow):
    await msg.channel.send(meowSeparate(msg.content)) 

  if any(word in msg.content for word in WithoutMe):
   await msg.channel.send("without me? :pleading_face:") 

try:
  token = os.getenv("Token") or ""
  if token == "":
    raise Exception("Please add your token to the Secrets pane.")
  client.run(token)
except discord.HTTPException as e:
    if e.status == 429:
        print(
            "The Discord servers denied the connection for making too many requests"
        )
        print(
            "Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests"
        )
    else:
        raise e
