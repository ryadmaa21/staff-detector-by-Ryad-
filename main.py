import os
import discord
import requests
import asyncio

TOKEN = os.getenv("DISCORD_TOKEN")  # sécurisé
CHANNEL_ID = 1361728242909843567

intents = discord.Intents.default()
client = discord.Client(intents=intents)

roblox_users = {
    "YT_GoraPlays": 1695670981,
    "YoZevStar": 1049767300,
    "GorillaWithASuit": 514679433,
    "VictoryForLife2468": 839818760,
    "Erin_Ireland22": 2465133159,
    "chasemaser": 22808138,
    "IIIllIllllllllIIIII": 7876617827,
    "lIllllllllllIllIIlll": 5728889572,
    "nwr_kr": 7980147812,
    "IlIIIlllllIIIIlIIIIl": 7574577126,
    "3MEWMTS5LJCB": 240526951,
    "Zengoulen": 1160595313,
    "nwrkr": 307212658,
    "OrionYeets": 547598710,
    "liilliilliiiliill": 2431747703,
    "lIIlIlIllllllIIlI": 5097000699,
    "wsgsponge": 376388734,
    "WMASZJOIDGKLLIOAMIOA": 123456789
}

def get_roblox_status(user_id):
    try:
        url = "https://presence.roblox.com/v1/presence/users"
        headers = {"Content-Type": "application/json"}
        res = requests.post(url, headers=headers, json={"userIds": [user_id]})
        if res.status_code != 200:
            return "⚠️ Request Failed"
        data = res.json()["userPresences"][0]
        status_type = data.get("userPresenceType")

        if status_type == 0:
            return "🔴 Offline"
        elif status_type == 1:
            return "🔵 Online (Website)"
        elif status_type == 2:
            return "🟢 In-Game (Unknown Game)"
        elif status_type == 3:
            return "🟢 In-Studio"
        else:
            return "❓ Unknown"
    except Exception as e:
        return "⚠️ Request Failed"

@client.event
async def on_ready():
    print(f"Connecté en tant que {client.user}")
    channel = client.get_channel(CHANNEL_ID)
    
    message = await channel.send("Chargement...")

    while True:
        status_lines = ["**Roblox Staff Status Update**\n"]
        for name, user_id in roblox_users.items():
            status = get_roblox_status(user_id)
            status_lines.append(f"**{name}**: {user_id}\n{status}\n")
        
        status_lines.append("🔄 Prochaine mise à jour dans 30s...")
        await message.edit(content="\n".join(status_lines))
        await asyncio.sleep(30)

client.run(TOKEN)

