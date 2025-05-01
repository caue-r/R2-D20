import discord
from discord.ext import commands
import random
import re


intents = discord.Intents.default()
intents.message_content = True

# Prefixo '!'
bot = commands.Bot(command_prefix='!', intents=intents)

escutando_iniciativas = False
iniciativas = []

@bot.event
async def on_ready():
    print(f'{bot.user.name} está online!')

# Coleta de iniciativas
@bot.command(name='iniciativa')
async def iniciar_iniciativa(ctx):
    global escutando_iniciativas, iniciativas
    iniciativas = []  # limpa a lista
    escutando_iniciativas = True
    await ctx.send("📝 R2-D20 está escutando as iniciativas! Use `D+X Nome`, `V+X Nome` ou `i+X Nome`. Encerre com `!stop`.")


@bot.command(name='stop')
async def parar_iniciativa(ctx):
    global escutando_iniciativas
    escutando_iniciativas = False

    if not iniciativas:
        await ctx.send("Nenhuma iniciativa registrada.")
        return

    # Ordena as iniciativas
    iniciativas.sort(key=lambda x: x['valor'], reverse=True)

    # Tabela de iniciativas
    tabela = "**📊 Iniciativas:**\n"
    for i, ini in enumerate(iniciativas, 1):
        tabela += f"**{i}.** {ini['nome']} → `{ini['detalhes']}` = **{ini['valor']}**\n"

    await ctx.send(tabela)

@bot.event
async def on_message(message):
    await bot.process_commands(message)

    global escutando_iniciativas
    if not escutando_iniciativas or message.author.bot:
        return

    # D, V ou i no início - Seguido de +X ou -X e depois o nome
    padrao = r'^(D|V|i)([+-]?\d+)\s+(.+)$'
    match = re.match(padrao, message.content.strip(), re.IGNORECASE)
    if not match:
        return

    prefixo, modificador_str, nome = match.groups()
    prefixo = prefixo.lower()
    modificador = int(modificador_str)
    nome = nome.strip()

    if prefixo == 'd':
        rolagens = [random.randint(1, 20) for _ in range(2)]
        mantido = min(rolagens)
        detalhes = f"Desvantagem: {rolagens} + ({modificador})"
    elif prefixo == 'v':
        rolagens = [random.randint(1, 20) for _ in range(2)]
        mantido = max(rolagens)
        detalhes = f"Vantagem: {rolagens} + ({modificador})"
    else:  # 'i'
        mantido = random.randint(1, 20)
        detalhes = f"Rolagem normal: [{mantido}] + ({modificador})"

    total = mantido + modificador
    iniciativas.append({'nome': nome, 'valor': total, 'detalhes': detalhes})
    await message.channel.send(f"🎲 {nome} registrou iniciativa: `{detalhes}` = **{total}**")



bot.run("INSIRA SEU TOKEN")

