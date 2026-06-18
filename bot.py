import discord
from discord.ext import commands
import os

# Configuración inicial del bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Sistema de Inteligencia Artificial Conectado: {bot.user}')

# Este evento es el "cerebro" que responde a todo de forma natural
@bot.event
async def on_message(message):
    # El bot no responde a sí mismo para evitar bucles
    if message.author == bot.user:
        return

    # Si escribes 'hola', responde con personalidad
    if message.content.lower().startswith("hola"):
        await message.channel.send("¡Saludos, Comandante! Estoy aquí, procesando datos y a tu entera disposición. ¿Qué misión tienes para mí hoy?")
    
    # Si escribes cualquier otra cosa larga, responde como IA
    elif len(message.content) > 3:
        await message.channel.send(f"Entendido, Comandante. Analizando: '{message.content}'. Mi lógica está procesando esta información para darte la mejor respuesta posible. ¿En qué más puedo asistirte?")

    await bot.process_commands(message)

# Ejecución del sistema
token = os.environ['DISCORD_TOKEN']
bot.run(token)

