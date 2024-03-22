import discord
from discord import Option
import random
import asyncio

TOKEN = 'ここにbotのトークンを入れる'
DISCORD_SERVER_IDS = ここにサーバーのIDを入れる

client = discord.Bot()

@client.event
async def on_ready():
    print(f"{client.user} コマンド待機中...")

@bot.slash_command(description="おみくじ", guild_ids=[DISCORD_SERVER_IDS])
async def omikuji(
    ctx: discord.ApplicationContext
):
    mikujidake = ['大吉', '吉', '中吉', '小吉', '末吉', '凶', '大凶']
    name = ctx.author.display_name
    id = str(ctx.author.id)
    def check():
        with open("omikuji.txt") as omikuji_f:
            datafile = omikuji_f.readlines()
        for line in datafile:
            if id in line:
                return True
        return False
    if check():
        await ctx.respond(f"1日1回まで！")
    else:
        f = open('omikuji.txt', 'a')
        f.write(f'{id}\n')
        f.close()
        await ctx.respond(f"{name}さんの運勢は...")
        await ctx.send(file=discord.File('omikuji.gif'), delete_after=5)
        await asyncio.sleep(5)
        result = random.choice(mikujidake)
        if result == "大吉":
            omikuji = "https://3.bp.blogspot.com/-vQSPQf-ytsc/T3K7QM3qaQI/AAAAAAAAE-s/6SB2q7ltxwg/s400/omikuji_daikichi.png"
            title = "大吉です！！"
        elif result == "吉":
            omikuji = "https://2.bp.blogspot.com/-27IG0CNV-ZE/VKYfn_1-ycI/AAAAAAAAqXw/fr6Y72lOP9s/s400/omikuji_kichi.png"
            title = "吉です！"
        elif result == "中吉":
            omikuji = "https://3.bp.blogspot.com/-_z-n-7gO3KA/T3K7MU3MdGI/AAAAAAAAE-k/8qs-jxqS4LE/s1600/omikuji_chuukichi.png"
            title = "中吉です"
        elif result == "小吉":
            omikuji = "https://3.bp.blogspot.com/-nZt5pjGWT9E/T3K7TJ4wEZI/AAAAAAAAE_E/c1X2-N54EYo/s1600/omikuji_syoukichi.png"
            title = "小吉です"
        elif result == "末吉":
            omikuji = "https://3.bp.blogspot.com/-JLNa8mwZRnU/T3K7StR-bEI/AAAAAAAAE-8/rQrDomz5MSw/s1600/omikuji_suekichi.png"
            title = "末吉です"
        elif result == "凶":
            omikuji = "https://4.bp.blogspot.com/-qCfF4H7YOvE/T3K7R5ZjQVI/AAAAAAAAE-4/Hd1u2tzMG3Q/s1600/omikuji_kyou.png"
            title = "凶です..."
        else:
            omikuji = "https://2.bp.blogspot.com/-h61ngruj0tE/T3K7RDUWmPI/AAAAAAAAE-0/KXtPY8fDwco/s1600/omikuji_daikyou.png"
            title = "大凶です......"
        color = random.choice(luckycolor)
        if color == "白色":
            ec = 0xE9ECEC
        elif color == "薄灰色":
            ec = 0x8E8E86
        elif color == "灰色":
            ec = 0x3E4447
        elif color == "黒色":
            ec = 0x141519
        elif color == "茶色":
            ec = 0x724728
        elif color == "赤色":
            ec = 0xA12722
        elif color == "橙色":
            ec = 0xF07613
        elif color == "黄色":
            ec = 0xF8C627
        elif color == "黄緑色":
            ec = 0x70B919
        elif color == "緑色":
            ec = 0x546D1B
        elif color == "青緑色":
            ec = 0x158991
        elif color == "空色":
            ec = 0x3AAFD9
        elif color == "青色":
            ec = 0x35399D
        elif color == "紫色":
            ec = 0x792AAC
        elif color == "赤紫色":
            ec = 0xBD44B3
        else:
            ec = 0xED8DAC
        embed = discord.Embed(color=ec, title=title, description=(f"ラッキカラーは{color}です！"))
        embed.set_thumbnail(url=omikuji)
        await ctx.send(embed=embed)

client.run(TOKEN)
