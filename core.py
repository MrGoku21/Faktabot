import discord
from discord.ext import commands
import math

# Etter stunder så kan du legge til libs ved å importere dem!

client = commands.Bot(command_prefix = "!", help_command=None) # Der du ser command_prefix = "!", den kan du endre til hva som helst. Men KUN ENDRE DET SOM ER INNI ALTSÅ ! IKKE FJERN " "

@client.event
async def on_ready():
    latency = math.ceil(client.latency * 1000) # Gir deg hvor mange ping botten er på, registert i ms (milisekund)
    name = client.user.name # Bottens navn vil bli displayed nedenfor!
    guild = client.guilds 
    users = len(client.users)
    server = len(guild) # Returns hvor mange guilds botten er i
    print("")
    print(f"Now running {name} on {server} servers \nCurrent websocket is {latency}ms\nCurrently watching over {users}") # Du kan endre deler av meldingen, men om du ikke kan discord.py så anbefaler jeg at du ikke gjør en dritt
    print("")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{server} servers | ")) # Du kan endre meldingen til hva du vil, men legg til {server} for å få antall servere botten er koblet til

@client.command()
async def reload(ctx, *, module : str = None): # Reloader etter endring i en kode i en fil, Usage !reload (filnavn)
    user = ctx.message.author
    if user.id == 209692111858171904: # Nå er den registert til Caasi sin ID, du skal endre den til din egen ID. Ikke gi den til noen andre!
        client.unload_extension(module)
        client.load_extension(module)
        await ctx.send(f"Reload on ``{module}`` completed!")
    if user.id != 209692111858171904: # Hvis andre folk prøver seg så får de en feil melding 
        await ctx.send("Only ``the owner`` can access this command!")

@client.command()
async def load(ctx, *, module : str): # Laster inn en fil hvis noe har skjedd, Usage !load (filnavn)
    user = ctx.message.author
    if user.id == 209692111858171904: # Nå er den registert til Caasi sin ID, du skal endre den til din egen ID. Ikke gi den til noen andre!
        client.load_extension(module)
        await ctx.send(f"Load on ``{module}`` completed!")
    if user.id != 209692111858171904: # Hvis andre folk prøver seg så får de en feil melding 
        await ctx.send("Only ``the owner`` can access this command!")

@client.command()
async def unload(ctx, *, module : str): #  Hvis du vil fjerne en fil fra botten så kan du unloade den, Usage !unload (filnavn)
    user = ctx.message.author
    if user.id == 209692111858171904: # Nå er den registert til Caasi sin ID, du skal endre den til din egen ID. Ikke gi den til noen andre!
        client.unload_extension(module)
        await ctx.send(f"Unload on ``{module}`` completed!")
    if user.id != 209692111858171904: # Hvis andre folk prøver seg så får de en feil melding 
        await ctx.send("Only ``the owner`` can access this command!")

client.load_extension('algorithm') # Her så sammenkobler den filen "algorithm" med selve kjærnen av botten!

client.run(" ") # Legg til din client.id her!
