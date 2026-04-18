import discord
from discord.ext import commands
from discord import app_commands
import os
import uuid
from dotenv import load_dotenv
from src.database.models import db

load_dotenv()

# Configuração do bot
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Bot conectado como {bot.user}')
    try:
        synced = await bot.tree.sync()
        print(f'✅ {len(synced)} Slash commands sincronizados')
    except Exception as e:
        print(f'❌ Erro ao sincronizar commands: {e}')
    await bot.change_presence(activity=discord.Game(name="/pix | /status"))

@bot.tree.command(name='pix', description='Criar uma nova transação PIX com valor')
@app_commands.describe(valor="Valor da venda em reais (ex: 150.00)")
async def pix_command(interaction: discord.Interaction, valor: str):
    """Comando para criar uma nova transação PIX"""
    
    await interaction.response.defer()
    
    try:
        # Converter para float
        valor_float = float(valor.replace(',', '.'))
    except ValueError:
        await interaction.followup.send("❌ Valor inválido! Use números (ex: 100.50)")
        return
    
    if valor_float <= 0:
        await interaction.followup.send("❌ O valor deve ser maior que 0!")
        return
    
    # Gerar chave PIX
    chave_pix = f"00020126360014br.gov.bcb.pix0136{str(uuid.uuid4())[:32]}52040000530398654061{valor_float:.2f}5802BR5913VENDEDOR6009SAO PAULO62410503***63041D3D"
    
    # Criar transação no banco de dados
    transaction_id = db.criar_transacao(
        valor=valor_float,
        chave_pix=chave_pix,
        channel_id=str(interaction.channel.id),
        usuario_id=str(interaction.user.id)
    )
    
    # Criar embed da mensagem
    embed = discord.Embed(
        title="💳 PIX Gerado",
        description=f"Transação ID: `{transaction_id}`",
        color=discord.Color.green()
    )
    embed.add_field(name="💰 Valor", value=f"R$ {valor_float:.2f}", inline=False)
    embed.add_field(name="🔑 Chave PIX", value=f"`{chave_pix}`", inline=False)
    embed.add_field(name="📋 Instruções", value="Copie a chave acima e cole no seu banco para realizar o pagamento", inline=False)
    embed.set_footer(text=f"ID: {transaction_id}")
    
    await interaction.followup.send(embed=embed)


@bot.tree.command(name='status', description='Verificar o status de uma transação')
@app_commands.describe(transaction_id="ID da transação (ex: a1b2c3d4)")
async def status_command(interaction: discord.Interaction, transaction_id: str):
    """Comando para verificar o status de uma transação"""
    
    await interaction.response.defer()
    
    # Buscar transação no banco
    transacao = db.obter_transacao(transaction_id)
    
    if not transacao:
        await interaction.followup.send(f"❌ Transação `{transaction_id}` não encontrada!")
        return
    
    # Definir cor e emoji baseado no status
    status_map = {
        'pendente': ('🟡 Pendente', discord.Color.yellow()),
        'processando': ('⏳ Processando', discord.Color.blue()),
        'aprovada': ('✅ Aprovada', discord.Color.green()),
        'recusada': ('❌ Recusada', discord.Color.red())
    }
    
    status_texto, cor = status_map.get(transacao['status'], ('❓ Desconhecido', discord.Color.greyple()))
    
    # Criar embed
    embed = discord.Embed(
        title="📊 Status da Transação",
        color=cor
    )
    embed.add_field(name="ID", value=f"`{transacao['id']}`", inline=False)
    embed.add_field(name="Valor", value=f"R$ {transacao['valor']:.2f}", inline=True)
    embed.add_field(name="Status", value=status_texto, inline=True)
    embed.add_field(name="Data", value=transacao['data_criacao'], inline=False)
    
    if transacao['motivo_rejeicao']:
        embed.add_field(name="Motivo da Rejeição", value=transacao['motivo_rejeicao'], inline=False)
    
    await interaction.followup.send(embed=embed)

# Função para iniciar o bot
def run_bot():
    token = os.getenv('DISCORD_TOKEN')
    if not token:
        print("❌ DISCORD_TOKEN não configurado no .env")
        return
    
    bot.run(token)
