from dotenv import load_dotenv
import os
import discord
from discord import Intents
import urllib.request
import numpy as np

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = Intents.default()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    # Get the list of members in the server
    guildId = 198871224808505346
    members = client.get_all_members()

    print(members)

    # Iterate through the list of members
    for member in members:
        # Get the avatar URL
        print(member.display_name)


client.run(TOKEN)
