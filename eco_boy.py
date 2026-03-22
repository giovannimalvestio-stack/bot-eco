
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


@bot.command()
async def ricette_eco(ctx):
    ricette=[
        "Polpette di pane: Pane raffermo ammollato nel latte, strizzato e mescolato con uova, prezzemolo e pecorino.",
        "Panzanella: Insalata estiva dell'Italia centrale con pane raffermo, pomodori, cipolla e cetrioli.",
        "Zuppa/Passato svuotafrigo: Verdure appassite bollite e frullate, ottime con aggiunta di crostini.",
        "Frittata di pasta o riso: Pasta o riso avanzati saltati in padella con uova sbattute e formaggio.",
        "Quiche o Torta salata: Sfoglia ripiena di verdure avanzate, salumi o formaggi in scadenza.",
        "Mondeghili: Polpette milanesi tipiche a base di carne bollita avanzata.",
        "Banana Bread: Dolce perfetto per utilizzare banane molto mature.",
        "Crostata del riciclo: Biscotti o fette biscottate sbriciolate, mischiate a marmellate miste avanzate",
        "Brodo vegetale: Bollire bucce, gambi e foglie di verdure (carote, sedano, cipolle) per un brodo corroborante",
        "Canederli: Gnocchi di pane tipici del Trentino-Alto Adige, arricchiti con speck o formaggio",
         ]
    ric=random.choice(ricette)
    await ctx.send(ric)


@bot.command()
async def rice_eco(ctx,ingrediente="pomodoro"):
    rifiti={
            "pomodoro": "Pappa al pomodoro: Zuppa rustica toscana perfetta per riciclare pomodori molto maturi e pane raffermo.",
            "patata": "Polpette di patate: Impastate le patate con uova, parmigiano e pangrattato, poi fritte o al forno.",
            "pane": "Canederli (Knödel) allo Speck: Gnocchi di pane, speck, latte, uova e prezzemolo, serviti in brodo.",
            "carne": "Polpettone di carne ripieno: Ottimo per utilizzare il lesso o l'arrosto, ideale ripieno di uova sode, verdure o formaggi.",
            "melanzana": "Parmigiana di melanzane veloce: Uno strato sottile di melanzane avanzate con pomodoro, mozzarella e basilico, cotto in poco tempo in forno o padella.",
            "pasta": "Pasta al forno filante: Mescola la pasta con besciamella, mozzarella e parmigiano, poi passa in forno finché non fa la crosticina."

            }
    tio=rifiti[ingrediente]
    await ctx.send(f"con il/la {ingrediente} si puo' fare la ricetta {tio}")


@bot.command()
async def deter_eco(ctx):
    detergenti=[
            "Detersivo Lavatrice al Sapone di Marsiglia: Sciogliere 100g di sapone di Marsiglia grattugiato in 2 litri d'acqua calda, aggiungere 2 cucchiai di bicarbonato.",
            "Ammorbidente all'Acido Citrico: Sciogliere 100g di acido citrico in 1 litro d'acqua distillata. Utilizzare 100ml nella vaschetta.",
            "Detersivo Piatti agli Agrumi: Frullare 4 limoni con 400ml d'acqua, 200g di sale e 100ml di aceto bianco; far bollire 10 min.",
            "Sgrassatore Universale Aceto e Limone: Mescolare 500ml d'acqua, 200ml di aceto bianco e il succo di un limone in uno spruzzino.",
            "Detergente Lavavetri e Specchi: Unire 1 litro d'acqua, 2 cucchiai di aceto e 5-10 gocce di olio essenziale (limone o eucalipto).",
            "Pasta Sgrassante per Forno: Creare una pasta con bicarbonato di sodio, un po' d'acqua e qualche goccia di sapone di Marsiglia, stendere e lasciare agire.",
            "Brillantante per Lavastoviglie: Soluzione al 15% di acido citrico (150g in 1 litro d'acqua).",
            "Detergente Pavimenti al Sapone Alga: Sciogliere 2 cucchiai di Sapone Alga in un secchio d'acqua calda.",
            "Spray Multiuso Acqua Ossigenata: 100ml alcool etilico, 200ml acqua ossigenata (10 vol), 200ml acqua demineralizzata.",
            "Detersivo WC Disincrostante: Versare 1 tazza di acido citrico in polvere o aceto caldo nel WC, lasciare agire tutta la notte."
         ]
    ric=random.choice(detergenti)
    await ctx.send(ric)







bot.run("IL TUO TOKEN")
            }
    tipo=rifiuti[rifiuto]
    await ctx.send(f"il {rifiuto} va nel {tipo} " )
