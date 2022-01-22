import requests
import discord

class blockData:
    async def blockdata(msg,APIkey,APIhost):
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
            embed=discord.Embed(title="挖掘數據記錄系統", description=json["response"], color=0xf5ec00)
            await msg.reply(embed=embed)
