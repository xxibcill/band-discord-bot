from array import array
import os
import string
from dotenv import load_dotenv
load_dotenv()
import query

# This example requires the 'members' and 'message_content' privileged intents to function.

import discord
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.messages = True

bot = commands.Bot(command_prefix='!', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def echo(ctx, txt: str):
    """just Echo"""
    await ctx.send(f"echo {txt}")

@bot.command()
async def price(ctx, symbol: str):
    """get reference data by provide 1 symbol"""
    await ctx.send(query.ger_ref_data([f"{symbol}/USD"])[0].rate)

@bot.command()
async def oraclescript(ctx, id: int):
    """show oracle script infomation by id"""
    oracle_script = query.get_oracle_script(id)
    embed=discord.Embed(
        title=f"Oracle Script #{id} {oracle_script.name}",
        url=f"https://cosmoscan.io/oracle-script/{id}",
        description=oracle_script.description,
        color=discord.Color.blue()
    )
    embed.add_field(name="**owner**", value=oracle_script.owner, inline=False)
    embed.add_field(name="**filename**", value=oracle_script.filename, inline=False)
    embed.add_field(name="**schema**", value=f"`{oracle_script.schema}`", inline=False)
    embed.add_field(name="**sourceCodeUrl**", value=oracle_script.source_code_url, inline=False)
    
    await ctx.channel.send(embed=embed)

@bot.command()
async def datasource(ctx, id: int):
    """show datasource infomation by id"""
    oracle_script = query.get_data_source(id)
    embed=discord.Embed(
        title=f"Oracle Script #{id} {oracle_script.name}",
        url=f"https://cosmoscan.io/data-source/{id}",
        description=oracle_script.description,
        color=discord.Color.blue()
    )
    embed.add_field(name="**owner**", value=f"[{oracle_script.owner}](https://cosmoscan.io/account/{oracle_script.owner})", inline=False)
    embed.add_field(name="**filename**", value=oracle_script.filename, inline=False)
    embed.add_field(name="**treasury**", value=f"[{oracle_script.treasury}](https://cosmoscan.io/account/{oracle_script.treasury})", inline=False)
    
    await ctx.channel.send(embed=embed)



bot.run(os.getenv('TOKEN'))

# print(query.get_data_source(111))

