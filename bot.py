import discord 
import os
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '?')

@client.event
async def on_ready():
  print('Bot is online.')

@client.command()
async def ping(ctx):
  await ctx.send(f'Pong! {round(client.latency * 1000)}ms.')


@client.event 
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send('Invalid command.')



@client.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount : int):
  await ctx.message.delete()
  await ctx.channel.purge(limit=amount)


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
  await member.kick(reason=reason)

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
  await member.ban(reason=reason)
  await ctx.send(f'Banned {member.mention}' + '.')


@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
  banned_users = await ctx.guild.bans()
  member_name, member_discriminator = member.split('#')

  for ban_entry in banned_users:
    user = ban_entry.user

    if (user.name, user.discriminator) == (member_name, member_discriminator):
      await ctx.guild.unban(user)
      await ctx.send(f'Unbanned {user.mention}' + '.')
      return

@client.command()
async def hello(ctx):
 await ctx.send('Hello, I am RemoteUtilities.')




client.run('OTI3Mzg3MjMwODU3NzQ4NTEx.YdJeqQ.w4vmrUE1nlzb0AKzbTkWrJ-RgFg')