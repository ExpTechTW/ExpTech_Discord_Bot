import requests

class md5:
    async def md5(msg,APIkey,APIhost):
        if msg.content.startswith("$md5"):
            data = {
                "APIkey": APIkey,
                "Function": "et",
                "Type": "md5",
                "FormatVersion": 1,
                "Value": msg.content.replace("$md5 ","")
            }

            header = {"content-type": "application/json"}
            response = requests.post(APIhost, json=data,headers=header, verify=False)
            json = response.json()
            print(json)
            await msg.reply(json["response"])
                            
