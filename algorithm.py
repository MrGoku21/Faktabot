import discord
from discord.ext import commands
import random
import datetime
import math


class algorithm(commands.Cog, name="algorithm"):
    def __init__(self, bot):
        self.bot = bot

    try:
        @commands.command() # Basic ping kommando
        async def ping(self, ctx):
            latency = math.ceil(self.bot.latency * 1000)
            member = ctx.message.author
            pfp = member.avatar_url
            embed=discord.Embed(title="Pong!", color=0x36393E)
            embed.add_field(name="The bots current websocket latency", value=f"{latency}ms", inline=False)
            embed.set_footer(text=f"Requested by {member}", icon_url=f"{pfp}")
            await ctx.send(embed=embed)

        @commands.command()
        async def fact(self, ctx, fact = None):
            if fact is None:
                await ctx.send("Hmmm, looks like you didn't tell me which fact to look up for!\nUsage: ``!fact (thing)``")
                return


            if fact == "kissa": # Kopier hele denne if statementen til return. Da kan du legge til flere facts!
                fact_list = [ 
                    'Kissa was born on August 1996', # Inni her kan du legge til din egen fakta!
                    'Kissa is a bug hunter', # Tips, vil du ha flere enn 3 faktas? under den siste (3) fakta så trykker du enter også legge du til '', og skriver inni. 
                    'Kissa means richboy in Norwegian',
                ]

                choose_fact = random.choice(fact_list) # Velger en random fact og lagrer den i veriablen, choose_fact


            if fact == "Bitcoin":
                fact_list = [ 
                    'Bitcoin er en cryptovaluta', 
                    'Bitcoin verdi kan øke eller minke',
                    'Bitcoin er laget av noen japanere',
                ]

                choose_fact = random.choice(fact_list) 


            else:
                await ctx.send(f"Sorry, I don't have any facts for, {fact}.\nTry ``!facts``") # Hvis ingen av faktaene ble funnet så sender den en feil melding


            member = ctx.message.author # Gir deg navnet på personen som brukte botten
            pfp = member.avatar_url # Gir deg profil bildet dems
            today = datetime.datetime.utcnow() 
            now = today.strftime("%A, %B %d %Y @ %H:%M") # Gir deg klokkeslett og dag personen brukte botten!

            # ----------------------------------------------------------------
            # Selve embeden!
            # -> Title | title er det første folk kan lese
            # -> Description | Description er det som er under selve titelen
            # -> Footer | footer er det siste folk kan lese
            # ----------------------------------------------------------------

            embed=discord.Embed(title=f"A random fact for {fact}", description=f"Did you know that\n{choose_fact}", color=0x36393E) 
            embed.set_footer(text=f"Requested by {member}\n{now}", icon_url=f"{pfp}")
            await ctx.send(embed=embed)

        @commands.command()
        async def facts(self, ctx):
            embed=discord.Embed(title=f"List of available facts", color=0x36393E)
            embed.add_field(name="Kissa", value=f"Gives you random facts about kissa!", inline=False)
            embed.add_field(name="Bitcoin", value=f"Gives you random facts about Bitcoin!", inline=False)  
            embed.set_footer(text=f"Requested by {member}\n{now}", icon_url=f"{pfp}")
            await ctx.send(embed=embed)

        except discord


def setup(bot):
    bot.add_cog(algorithm(bot))


