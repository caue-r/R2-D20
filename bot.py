from dotenv import load_dotenv
import os
load_dotenv()
import discord
from discord.ext import commands
import random
import re

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

escutando_iniciativas = False
iniciativas = []

@bot.event
async def on_ready():
    print(f'{bot.user.name} está online!')

# Comando de ajuda
@bot.command(name='ajuda')
async def ajuda(ctx):
    embed = discord.Embed(
        title="📘 Comandos do R2-D20",
        description="Aqui estão os comandos disponíveis:",
        color=discord.Color.blue()
    )
    embed.add_field(
        name="!iniciativa",
        value="Começa a escutar iniciativas. Use `D+X Nome`, `V+X Nome` ou `i+X Nome` para registrar.\n- `D` = Desvantagem\n- `V` = Vantagem\n- `i` = Rolagem normal",
        inline=False
    )
    embed.add_field(
        name="!roll",
        value="Rola dados no formato `xdy`, exemplo: `3d6`, `1d20+3` ou `2#d20`. Para rolar sem somar, use `x#dy`.",
        inline=False
    )
    embed.add_field(
        name="!stop",
        value="Para de escutar e mostra a tabela de iniciativas registradas.",
        inline=False
    )
    embed.add_field(
        name="!ajuda",
        value="Mostra esta mensagem de ajuda.",
        inline=False
    )

    await ctx.send(embed=embed)

# Rolagem de dados
@bot.command(name='roll')
async def rolar_dados(ctx, *, dados: str):   
    padrao = r'^(\d+)(#)?d(\d+)([+-]\d+)?$'
    match = re.match(padrao, dados)
    if not match:
        await ctx.send("Formato inválido! Use xdy, xdy+z ou x#dy, exemplo: 2d6, 1d20+3 ou 3#d20.")
        return

    quantidade, separar, lados, modificador = match.groups()
    quantidade = int(quantidade)
    lados = int(lados)
    modificador = int(modificador) if modificador else 0
    resultados = [random.randint(1, lados) for _ in range(quantidade)]
    soma = sum(resultados) + modificador

    # Configuração de cor e mensagem para rolagens críticas
    cor = discord.Color.blue()
    mensagem_critica = ""
    if lados == 20 and quantidade == 1:
        if resultados[0] == 1:
            cor = discord.Color.red()
            mensagem_critica = "💥 Falha Crítica!"
        elif resultados[0] == 20:
            cor = discord.Color.green()
            mensagem_critica = "✨ Sucesso Crítico!"

    embed = discord.Embed(
        title=f"🎲 Rolagem de {dados}",
        color=cor
    )

    if separar:
        if quantidade > 25:
            await ctx.send("🚫 O número máximo de dados exibidos separadamente é 25. Tente usar `xdy` para somar os resultados ou rolar menos dados.")
            return
        for i, resultado in enumerate(resultados):
            embed.add_field(name=f"Rolagem {i+1}", value=f"`[{resultado}] d{lados}`", inline=False)

    else:
        resultados_str = " | ".join([f"`[{r}] d{lados}`" for r in resultados])
        if len(resultados_str) > 1024:
            await ctx.send("🚫 O número de dados rolados excede o limite suportado pelo Discord. Tente rolar menos dados.")
            return
        embed.add_field(name="Resultados", value=resultados_str, inline=False)
        if modificador != 0:
            embed.add_field(name="Modificador", value=f"{modificador:+}", inline=False)
        embed.add_field(name="Soma", value=f"**{soma}**", inline=False)
        if mensagem_critica:
            embed.add_field(name="Mensagem", value=mensagem_critica, inline=False)

    await ctx.send(embed=embed)

# Iniciar iniciativa
@bot.command(name='iniciativa')
async def iniciar_iniciativa(ctx):
    global escutando_iniciativas, iniciativas
    iniciativas = []
    escutando_iniciativas = True
    await ctx.send("📝 R2-D20 está escutando as iniciativas! Use `D+X Nome`, `V+X Nome` ou `i+X Nome`. Encerre com `!stop`.")

# Parar iniciativa
@bot.command(name='stop')
async def parar_iniciativa(ctx):
    global escutando_iniciativas
    escutando_iniciativas = False

    if not iniciativas:
        await ctx.send("Nenhuma iniciativa registrada.")
        return

    iniciativas.sort(key=lambda x: x['valor'], reverse=True)

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
    else:
        mantido = random.randint(1, 20)
        detalhes = f"Rolagem normal: [{mantido}] + ({modificador})"

    total = mantido + modificador
    iniciativas.append({'nome': nome, 'valor': total, 'detalhes': detalhes})
    await message.channel.send(f"🎲 {nome} registrou iniciativa: `{detalhes}` = **{total}**")

bot.run(os.getenv("DISCORD_TOKEN"))
