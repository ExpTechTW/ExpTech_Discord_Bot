import requests
import discord

class inventory:
    async def inventory(msg,APIkey,APIhost):
        if msg.content == "$inventory":
            data = {
                "APIkey": APIkey,
                "Function": "serverData",
                "Type": "Inventory",
                "FormatVersion": 1,
                "Value": str(msg.author.id)
            }

            header = {"content-type": "application/json"}
            response = requests.post(APIhost, json=data,headers=header, verify=False)
            json = response.json()
            embed=discord.Embed(title="背包數據", description=json["response"], color=0xf5ec00)
            await msg.reply(embed=embed)

