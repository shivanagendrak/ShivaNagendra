import discord
from discord.ext import commands
from config import TOKEN

bot = commands.Bot(command_prefix="#" , case_insensitive = True , intents=discord.Intents.all(), self_bot = True)

@bot.command()
async def hi(ctx):
    await ctx.send(f"Hello {ctx.message.author}")

@bot.command()
async def ping(ctx):
    await ctx.send(f"Latency is {round((bot.latency)*1000)}ms")


@bot.event
async def on_ready():
    print("Bot is Ready!")





bot.run(TOKEN)