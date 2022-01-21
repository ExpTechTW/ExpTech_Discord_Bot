ver = "22w04-pre1-py"

# 本地
from config.config import config

# 依賴
import discord
import requests
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
    if msg.author.bot:
        return

    async def urlchecker():
        data = {
            "APIkey": APIkey,
            "Function": "et",
            "Type": "urlChecker",
            "FormatVersion": 1,
            "Value": msg.content
        }
        header = {"content-type": "application/json"}
        response = requests.post(APIhost, json=data,headers=header, verify=False)
        json = response.json()
        if json["response"] == "No URL found":
            return
        if json["state"] == "Success":
            if json["response"] == "All URL inspections passed":
                await msg.reply("文本中沒有危險網址")
            else:
                await msg.reply("文本中含有危險網址")
        else:
            print("錯誤: {}".format(json["response"]))

    await urlchecker()

    async def blockdata():
        if msg.content == "$block":
            data = {
                "APIkey": APIkey,
                "FormatVersion": 1,
                "Function": "serverData",
                "Type": "BlockValue",
                "Value": str(msg.author.id)
            }
            header = {"content-type": "application/json"}
            response = requests.post(APIhost, json=data,headers=header, verify=False)
            json = response.json()
            await msg.reply(json["response"])

    await blockdata()

client.run(config.token)