import discord
from discord.ext import commands
from config import TOKEN

bot = commands.Bot(command_prefix="#" , case_insensitive = True , intents=discord.Intents.all(), self_bot = True)

@bot.event
async def on_ready():
    print("Bot is Ready!")


bot.run(TOKEN)