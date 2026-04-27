import discord
import asyncio
from TikTokLive import TikTokLiveClient
from TikTokLive.events import LiveStartEvent

# ====== بياناتك ======
DISCORD_TOKEN = "MTQ5ODM5NTMxNTc1NjA3NzMxNg.GrYkFA.zJ791nH9xeDvUQln8cMdxWYKzTlg8VAIXhPthU"
CHANNEL_ID = 1435974535013728286
TIKTOK_USERNAME = ".chico97@"

# ====== ديسكورد ======
intents = discord.Intents.default()
client = discord.Client(intents=intents)

# ====== تيك توك لايف ======
tiktok = TikTokLiveClient(unique_id=TIKTOK_USERNAME)

sent = False

@tiktok.on(LiveStartEvent)
async def on_live_start(event):
    global sent
    if sent:
        return

    sent = True

    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("@everyone 🔴 بدأ بث مباشر على تيك توك!")

# ====== تشغيل البوت ======
@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

    # تشغيل مراقبة تيك توك
    asyncio.create_task(tiktok.start())

client.run(DISCORD_TOKEN)
