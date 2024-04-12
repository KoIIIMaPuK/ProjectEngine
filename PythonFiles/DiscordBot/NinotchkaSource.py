import disnake
from discord.ext import commands
from discord import Intents

with open("E:\FolderForProgrammingProject\ForNinotchka.txt", "r") as file:
    str_TokenNinotchka = file.readline()

intents = Intents.all()  # Use discord.Intents instead of disnake.Intents
housemaid = commands.Bot(command_prefix='$', intents=intents)

@housemaid.event
async def on_ready():
    print("i'm ready")

@housemaid.command()
async def ping(ctx):  # Use ctx instead of inter
    await ctx.send("Понг!")

housemaid.run(str_TokenNinotchka)