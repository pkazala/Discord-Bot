import discord
import os
import requests
import json
from keep_alive import keep_alive

client = discord.Client()

def ciekawostka():
  url = "https://numbersapi.p.rapidapi.com/random/trivia"

  querystring = {}

  headers = {
    'x-rapidapi-key': "ae340e5fadmsh0582d90cc25194fp14c141jsn7c9a511dc28f",
    'x-rapidapi-host': "numbersapi.p.rapidapi.com"
    }

  response = requests.request("GET", url, headers=headers, params=querystring)

  print(response.text)
  return(response.text)

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('ciekawostka'):
    quote = ciekawostka()
    await message.channel.send(quote)

keep_alive()
client.run(os.getenv('token'))