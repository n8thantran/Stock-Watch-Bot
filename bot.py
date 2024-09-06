import discord
from discord.ext import commands
import yfinance as yf

bot = commands.Bot(command_prefix='!')

def get_stock_info(symbol):
    try:
        stock = yf.Ticker(symbol)
        info = stock.info
        return {
            'Previous Close': info.get('previousClose', 'N/A'),
            'Open': info.get('open', 'N/A'),
            'Day’s Range': f"{info.get('dayLow', 'N/A')} - {info.get('dayHigh', 'N/A')}",
            'P/E Ratio': info.get('forwardPE', 'N/A')
        }
    except Exception as e:
        print("Error:", e)
        return None

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def stock(ctx, ticker: str):
    info = get_stock_info(ticker)

    if info is None:
        await ctx.send("Could not retrieve information for the ticker.")
        return

    embed = discord.Embed(title=f"Stock Information for {ticker.upper()}", color=discord.Color.blue())

    for key, value in info.items():
        embed.add_field(name=key, value=value, inline=False)

    await ctx.send(embed=embed)

TOKEN = 'YOUR_DISCORD_BOT_TOKEN'
bot.run(TOKEN)
