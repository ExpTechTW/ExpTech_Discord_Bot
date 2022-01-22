ver = "22w04-pre2-py"

#本地
from Python.config import config
from Python.urlChecker import urlChecker
from Python.blockData import blockData
from Python.inventory import inventory
from Python.md5 import md5


#依賴
import discord
client = discord.Client()
intents = discord.Intents.default()
intents.members = True
intents.voice_states = True
APIkey=config.APIkey
APIhost=config.APIhost


@client.event
async def on_ready():
    print('目前登入身份： {} !'.format(client.user))

@client.event
async def on_message(msg):
    if msg.author.bot: return
    await urlChecker.main(msg,APIkey,APIhost)
    await blockData.blockdata(msg,APIkey,APIhost)
    await inventory.inventory(msg,APIkey,APIhost)
    await md5.md5(msg,APIkey,APIhost)

if config.token!="Put Your Bot Token Here":
    client.run(config.token)
else:
    print("請在 config.py 放入機器人 Token")