
from discord import bot
from discord.ext import commands
from discord.ext.commands import bot
import discord
import asyncio
import random
import youtube_dl
import string
import os
from discord.ext import commands
from discord import message
import config
from pymongo import MongoClient


commands.Bot(...)
bot = commands.Bot(command_prefix=".")



@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("twitch.tv/iskanderrt"))


@bot.event
async def on_command_error(ctx, error):
    print(error)

    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.author.mention}, у вас недостаточно прав для выполнения данной команды!")
    elif isinstance(error, commands.UserInputError):
        await ctx.send(embed=discord.Embed(
            description=f"Правильное использование команды: {ctx.prefix}{ctx.command.name} ({ctx.command.brief})\nExample: {ctx.prefix}{ctx.command.usage}"
        ))

@bot.command(name="clear", brief="Очистить чат от сообщений, по умолчанию 10 сообщений", usage="clear <amount=10>")
@commands.has_permissions(manage_roles=True, ban_members=True)
async def clear_channel(ctx, amount: int=10):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"Was deleted {amount} messages...")
    await ctx.message.add_reaction("✅")


@bot.command(name="kick", brief="Выгнать пользователя с сервера", usage="kick <@user> <reason=None>")
@commands.has_permissions(kick_members=True)
async def kick_user(ctx, member: discord.Member, *, reason=None):
    await ctx.message.delete(delay=1)

    await member.send(f"You was kicked from server")
    await ctx.send(f"Member {member.mention} was kicked from this server!")
    await member.kick(reason=reason)
    await ctx.message.add_reaction("✅")


@bot.command(name="ban", brief="Забанить пользователя на сервере", usage="ban <@user> <reason=None>")
@commands.has_permissions(ban_members=True)
async def ban_user(ctx, member: discord.Member, *, reason=None):
    await member.send(f"You was banned on server")
    await ctx.send(f"Member {member.mention} was banned on this server")
    await member.ban(reason=reason)
    await ctx.message.add_reaction("✅")
    await ctx.message.delete(delay=1)

@bot.command(name="unban", brief="Разбанить пользователя на сервере", usage="unban <user_id>")
@commands.has_permissions(ban_members=True)
async def unban_user(ctx, user_id: int):
    user = await bot.fetch_user(user_id)
    await ctx.guild.unban(user)
    await ctx.message.add_reaction("✅")
    await ctx.message.delete(delay=1)
@bot.command(name="mute", brief="Запретить пользователю писать (настройте роль и канал)", usage="mute <member>")
@commands.has_permissions(kick_members=True)
async def mute_user(ctx, member: discord.Member):
    mute_role = discord.utils.get(ctx.message.guild.roles, name="Mute")
    await member.add_roles(mute_role)
    await ctx.send(f"{ctx.author} gave role mute to {member}")
    await ctx.message.add_reaction("✅")
    await ctx.message.delete(delay=1)
@bot.command(name="unmute", brief="Запретить пользователю писать (настройте роль и канал)", usage="mute <member>")
@commands.has_permissions(kick_members=True)
async def unmute_user(ctx, member: discord.Member):
    mute_role = discord.utils.get(ctx.message.guild.roles, name="Mute")
    await member.remove_roles(mute_role)
    await ctx.send(f"{ctx.author} remove role mute to {member}")
    await ctx.message.add_reaction("✅")
    await ctx.message.delete(delay=1)
@bot.command()
@commands.has_permissions(manage_roles=True, ban_members=True)
async def ping(ctx):
        await ctx.send(f"Pong! {round(bot.latency * 100)}ms")
        await ctx.message.add_reaction("✅")
        await ctx.message.delete(delay=1)
@bot.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
async def nick(ctx, member: discord.Member, nickname):
  await member.edit(nick=nickname)
  await ctx.message.add_reaction("✅")
  await ctx.message.delete(delay=1)

TOKEN = 'OTk3MTk5MzE3NDA2MzM5MTUy.GONZTt.BPLRH0EvSEU3cIot-i_sWMPFY3dhJ83u4Ve2C8'
bot.run(TOKEN)
