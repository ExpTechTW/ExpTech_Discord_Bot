import requests

class urlChecker:
    async def main(msg,APIkey,APIhost):
        Data = {
            "APIkey": APIkey,
            "Function": "et",
            "Type": "urlChecker",
            "FormatVersion": 1,
            "Value": msg.content
        }
        header = {"content-type": "application/json"}
        response = requests.post(APIhost, json=Data, headers=header, verify=False)
        Json = response.json()
        if Json["response"] == "No URL found": return
        if Json["state"] == "Success":
            if Json["response"] == "All URL inspections passed":
                await msg.add_reaction("✅")
            else:
                await msg.add_reaction("❌")
                await msg.reply("文本中含有危險網址")
                await msg.delete()
        else:
            print("錯誤: {}".format(Json["response"]))