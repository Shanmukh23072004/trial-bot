import discord
from discord.ext import commands
import requests

intents = discord.Intents.all()

intents.messages = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as interactive Bot')


@bot.command()
async def quote(ctx):

    response = requests.get('https://zenquotes.io/api/random')

    data = response.json()

    quote_text = data[0]['q']

    await ctx.send(quote_text)

    
@bot.command()
async def joke(ctx):
    # Make a request to the API
    response = requests.get('https://official-joke-api.appspot.com/random_joke')

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Extract the joke text and setup
        joke_setup = data['setup']
        joke_punchline = data['punchline']
        
        # Send the joke to the Discord channel
        await ctx.send(f"**Joke:**\n{joke_setup}\n{joke_punchline}")
    else:
        await ctx.send("Failed to fetch a joke.")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command. Type !help for a list of available commands.')


@bot.event
async def on_message(message):
    await bot.process_commands(message)

    if message.author.bot:
        return

    if not message.content.startswith(bot.command_prefix) and isinstance(message.channel, discord.DMChannel):
        await message.author.send("I'm a bot! Please use my commands in a server.")

bot.run("MTIxNjUxNjYzMzY3NDM4NzU1OA.GrZYI0.MFpSE7J7fnR8o9qdTmwBLdepzeqhwYx6iGm2jQ")
