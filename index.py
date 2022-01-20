ver="22w04-pre1-py"

#本地
from Python.config import config
from Python.urlChecker import urlChecker

#依賴
import discord
client = discord.Client()
intents = discord.Intents.default()
intents.members = True
intents.voice_states = True

@client.event
async def on_ready():
    print('目前登入身份： {} !'.format(client.user))

@client.event
async def on_message(msg):
    if msg.author.bot: return
    urlChecker.main(msg,config.APIkey,config.APIhost)

if config.token!="Put Your Bot Token Here":
    client.run(config.token)
else:
    print("請在 config.js 放入機器人 Token")