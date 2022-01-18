import discord
from discord.ext import commands
import os
import json

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix="#k", case_insensitive=True, intents=intents)

client.muted = False
with open("words.json", "r") as f:
        client.data = json.load(f)

@client.event
async def on_ready():
    print("Online")
    await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.listening, name="Kozmic"))

@client.event
async def on_message(message):
    if message.author.id == int("809877801774612490"):
        if client.muted == True:
            await message.delete()
        else:
            for x in client.data["words"]:
                if x in message.content:
                    await message.delete()
                    break
    else: 
        if message.content == "#kmute":
            if client.muted == False:
                client.muted = True
                await message.channel.send(":thumbsup: **Muted Kozmic lol**")
            else:
                client.muted = False
                await message.channel.send(":thumbsup: **Unmuted Kozmic.. why?**")
        elif "#kadd " in message.content:
            word = message.content[6:]
            if word in client.data["words"]:
                await message.channel.send(":exclamation: **Word already added**")
            else:
                client.data["words"].append(word)
                
                with open("words.json", "w") as f:
                    json.dump(client.data, f, indent=2)
                await message.channel.send(f':thumbsup: **Added "{word}"**')

client.run("OTMzMTMyNjI1NDgzMjY4MTQ4.YedFeg.V03kQ91H2vgDF9yAjaN18TXPb0I")   