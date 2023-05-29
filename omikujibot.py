import discord
from discord import Option
import random

TOKEN = 'ここにbotのトークンを入れる'
DISCORD_SERVER_IDS = ここにサーバーのIDを入れる

client = discord.Bot()

@client.event
async def on_ready():
    print(f"{client.user} コマンド待機中...")

@client.slash_command(description="おみくじコマンド", guild_ids=[DISCORD_SERVER_IDS])
async def omikuji(
    ctx: discord.ApplicationContext,
    name: Option(str, required=False, description="名前を入れてね")
):
    result = ['大吉', '吉', '中吉', '小吉', '末吉', '凶', '大凶']
    luckyitem = ['コーラ', 'サイダー', 'コーヒー', 'ハンカチ', 'ポケットティッシュ', 'バッグ', 'タオル', 'スイーツ', 'クリアファイル', '綿棒']
    name = name or ctx.author.name
    await ctx.respond(f"{name} さんの運勢は...{random.choice(result)}です！\nラッキーアイテムは{random.choice(luckyitem)}です！")

client.run(TOKEN)
