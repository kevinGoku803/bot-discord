import discord
import os
from discord.ext import commands

# Configuración del bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.command()
async def hola(ctx):
    await ctx.send('¡Hola, Comandante! El sistema está operativo.')

# Ejecución del bot usando una variable de entorno segura
# (Esto buscará el token en la configuración secreta de GitHub)
token = os.environ['DISCORD_TOKEN']
bot.run(token)
