import os
import subprocess
import discord
from discord import app_commands

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
SERVER_TOKEN = os.getenv('SERVER_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
#bot = commands.Bot(command_prefix='&', intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name='mc',description='Interact with notre-minecraft',guild=discord.Object(id=SERVER_TOKEN))
async def start_server(interaction, command:str):
    result = subprocess.run(['ragnamod.sh', command], stdout=subprocess.PIPE)
    await interaction.response.send_message(result.stdout)

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=SERVER_TOKEN))
    print('Connected')

client.run(DISCORD_TOKEN)
