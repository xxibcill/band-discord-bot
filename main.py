from array import array
import os
import string
from dotenv import load_dotenv
load_dotenv()
import query
from google.protobuf.json_format import MessageToJson

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

@bot.command()
async def blockheight(ctx):
    """get current block height"""
    await ctx.send(f"current block height is {query.get_block_height()}")

@bot.command()
async def sequence(ctx, address: str):
    """get sequence of address"""
    acc = query.get_account(address)
    if(acc != None):
        await ctx.send(f"current sequence of {address} is **{acc.sequence}**")
    else:
        await ctx.send(f"account **{address}** does not exist")

@bot.group()
async def transaction(ctx):
    """Transaction group command
        !transaction height <txhash> -> to get block of Tx
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')


@transaction.command(name='height')
async def _height(ctx,hash: str):
    """get block height of Tx"""
    await ctx.send(query.get_block_from_tx(hash))

@transaction.command(name='info')
async def _info(ctx,hash: str):
    """get transaction infomation"""
    tx = query.get_tx(hash)
    embed=discord.Embed(
        title=f"Transaction #{hash}",
        url=f"https://cosmoscan.io/tx/{hash}",
        color=discord.Color.blue()
    )
    embed.add_field(name="**Block**", value=tx.tx_response.height, inline=False)
    # embed.add_field(name="**Sender**", value=tx.tx_response.height, inline=False)
    
    await ctx.channel.send(embed=embed)

# bot.run(os.getenv('TOKEN'))

print(query.get_block_from_tx("ECDDD944CB366C9F6BD212E08B8F79313AFA2A7018EB545E7E808B299E4A4602"))


