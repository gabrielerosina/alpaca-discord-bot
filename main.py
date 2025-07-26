import alpaca_trade_api as tradeapi
import discord
import asyncio

ALPACA_KEY = "your_alpaca_key"
ALPACA_SECRET = "your_alpaca_secret"
DISCORD_TOKEN = "your_discord_token"
DISCORD_CHANNEL_ID = 123456789012345678  # Replace with your real channel ID

intents = discord.Intents.default()
client = discord.Client(intents=intents)

async def check_price_and_alert():
    api = tradeapi.REST(ALPACA_KEY, ALPACA_SECRET, base_url='https://paper-api.alpaca.markets')
    barset = api.get_bars('AAPL', 'minute', limit=1)
    latest_price = barset[-1].c

    if latest_price > 200:  # Example condition
        channel = client.get_channel(DISCORD_CHANNEL_ID)
        await channel.send(f"AAPL just hit ${latest_price}!")

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    while True:
        await check_price_and_alert()
        await asyncio.sleep(60)  # Check every minute

client.run(DISCORD_TOKEN)
