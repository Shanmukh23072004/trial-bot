import discord
from discord.ext import commands

intents = discord.Intents.all()

intents.messages = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as Admin Bot')

@bot.command()
async def hello(ctx):
    await ctx.send("Hi there!")

@bot.command()
async def how_are_you(ctx):
    await ctx.send("I'm doing well, thank you for asking.")

@bot.command()
async def bye(ctx):
    await ctx.send("Goodbye!")


@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    if ctx.author.guild_permissions.kick_members:
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} has been kicked.")
    else:
        await ctx.send("You don't have permission to kick members.")

@bot.event
async def on_message(message):
    await bot.process_commands(message)

    if message.author.bot:
        return

    if not message.content.startswith(bot.command_prefix) and isinstance(message.channel, discord.DMChannel):
        await message.author.send("I'm a bot! Please use my commands in a server.")

bot.run("MTIxNjUxNjYzMzY3NDM4NzU1OA.GrZYI0.MFpSE7J7fnR8o9qdTmwBLdepzeqhwYx6iGm2jQ")
