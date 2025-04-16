import os
import discord
import requests
import asyncio

TOKEN = "MTM2MTcxNzU2OTM0OTg3Nzg1MA.GeLJP9.9c2Wg9OqLhdW2ygZNbgrCFH3hoOWti_0rmgd24"
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
            return f"🟢 In-Game: {data.get('lastLocation')}"
        elif status_type == 3:
            return f"🟢 In-Studio: {data.get('lastLocation')}"
        else:
            return "❓ Unknown"
    except Exception as e:
        return f"⚠️ Request Failed"

async def update_status_loop():
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)

    if channel is None:
        print("❌ Channel introuvable. Vérifie l'ID.")
        return

    message = await channel.send("🟢 Initialisation...")

    while not client.is_closed():
        status_msg = "Roblox Staff Status Update\n\n"
        for username, user_id in roblox_users.items():
            status = get_roblox_status(user_id)
            status_msg += f"{username}: {user_id}\n{status}\n\n"

        status_msg += "🔄 Prochaine mise à jour dans 30s..."

        try:
            await message.edit(content=status_msg)
        except Exception as e:
            print("Erreur de mise à jour:", e)

        await asyncio.sleep(30)

@client.event
async def on_ready():
    print(f"✅ Connecté en tant que {client.user}")
    client.loop.create_task(update_status_loop())

client.run(TOKEN)
