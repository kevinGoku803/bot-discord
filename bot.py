import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Sistema en línea: {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    msg = message.content.lower()

    # Respuestas directas y naturales
    if "dos más dos" in msg:
        await message.channel.send("Pues cuatro, ¿no? ¿O me estás poniendo a prueba?")
    
    elif "hola" in msg or "qué tal" in msg:
        await message.channel.send("¡Hola! Aquí estoy, ¿qué cuentas?")
    
    elif len(msg) > 3:
        # Respuestas variadas que parecen una charla real
        respuestas = [
            "Eso suena bastante interesante, cuéntame más.",
            "Ya veo, tiene sentido. ¿Qué más tienes pensado?",
            "Vale, entiendo perfectamente.",
            "Interesante punto de vista. ¿Qué sigue ahora?",
            "La verdad es que sí, es una buena forma de verlo.",
            "¿Ah sí? No lo había visto desde ese ángulo."
        ]
        await message.channel.send(random.choice(respuestas))

    await bot.process_commands(message)

token = os.environ['DISCORD_TOKEN']
bot.run(token)
)

