import requests
import discord


class statistic:
    async def statistic(msg,APIkey,APIhost):
        if msg.content == "$statistic":
            data = {
                "APIkey": APIkey,
                "FormatVersion": 1,
                "Function": "serverData",
                "Type": "Statistic",
                "Value": str(msg.author.id)
            }
            header = {"content-type": "application/json"}
            response = requests.post(APIhost, json=data,headers=header, verify=False)
            Data = requests.get("https://raw.githubusercontent.com/ExpTechTW/API/%E4%B8%BB%E8%A6%81%E7%9A%84-(main)/Json/server/block.json")
            json = response.json()["response"]
            data=Data.json()
            MSG=""
            for x in range(len(json)):
                name=json[x]["name"]
                if(name != "USE_ITEM" and name != "ENTITY_KILLED_BY" and name != "KILL_ENTITY" and name != "BREAK_ITEM" and name != "DROP" and name != "PICKUP" and name != "CRAFT_ITEM" and name != "MINE_BLOCK"):
                    for i in range(len(data["Statistic"])):
                        if(data["Statistic"][i]["name"]==name):
                            MSG+="名稱: "+data["Statistic"][i]["zh-Hant-TW"]+" - 數量: "+str(json[x]["value"])+"\n"
                            break
            embed=discord.Embed(title="玩家各項統計數據", description=MSG, color=0xFFE4E1)
            await msg.reply(embed=embed)