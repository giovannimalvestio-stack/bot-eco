import discord
from discord.ext import commands
import random
import os

# la variabile intents contiene i permessi al bot
intents = discord.Intents.default()
# abilita il permesso a leggere i contenuti dei messaggi
intents.message_content = True
# crea un bot e passa gli indents

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hai fatto l\'accesso come {bot.user}')

@bot.command()
async def ciao(ctx):
    await ctx.send(f'Ciao! Sono un bot {bot.user}!')


@bot.command()
async def calendario(ctx):
    with open("cal.jpg","rb") as f:
        file=discord.File(f)
        await ctx.send(file=file)


@bot.command()
async def eco_cons(ctx):
    conss=[
        "Chiudere il rubinetto mentre ci si lava i denti, preferire la doccia al bagno, utilizzare la lavastoviglie a pieno carico e limitare i lavaggi auto.",
        "Evitare plastica monouso (posate, bicchieri), preferire prodotti sfusi, acquistare di seconda mano e ridurre lo spreco alimentare.",
        "Spegnere le luci inutilizzate, usare lampadine LED, passare a energie rinnovabili e ottimizzare il riscaldamento/raffreddamento.",
        "Preferire la bicicletta, i mezzi pubblici o il treno all'aereo e all'auto privata, specialmente per brevi tragitti.",
        "Leggere le etichette, scegliere prodotti locali (km 0), biologici e non nocivi per l'ambiente.",
        "Utilizzare borse in tela, coperchi in silicone, carta forno lavabile e involucri in cera d'api.",
        "Alleggerire i bagagli, ridurre i rifiuti e non lasciare tracce, rispettando gli habitat naturali."
        ]
    con=random.choice(conss)
    await ctx.send(con)


@bot.command()
async def dove_va(ctx,rifiuto="quaderno"):
    # dizionario che funziona con coppie chiavi e valori.
    # Per leggere il valore di una chiave si fa nome_dizionario['nome_chiave']
    rifiuti={
            "quaderno": "carta",
            "lattina": "metallo",
            "bottigliadi plastica": "plastica",
            "carta casa": "umido",
            "cartone": "carta",
            "cibo": "umido"

            }
    tipo=rifiuti[rifiuto]
    await ctx.send(f"il {rifiuto} va nel {tipo} " )
