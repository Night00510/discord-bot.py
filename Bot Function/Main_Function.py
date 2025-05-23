import discord
<<<<<<< HEAD
from Token import get_token #ใช้ชื่อฟังก์ชันที่ตั้ง
=======
from Token import get_token #ใช้ชื่อฟังก์ชันที่ตั้งให้ถูกด้วย
>>>>>>> 5b40d920f92b530ead073f56dfbecf31ecfd53b3
from discord.ext import commands
from random import randint

bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())

def make_embed(title, description): #embedร้วม
    return discord.Embed(title = title, description = description, color = randint(0, 0xFFFFFF)) #สุ่มสีส

#bot events
@bot.event
#bot พร้อม
async def on_ready():
    print("Bot is ready")

#คนเข้า-อกกเซิร์ฟ
@bot.event
#เข้า
async def on_member_join(member):
    channel = bot.get_channel(1120311887184277528) #IDห้อง
    await channel.send(embed=make_embed("ยินดีต้อนรับ", f"ยินดีต้อนรับ {member.mention}!"))
    await member.send(embed=make_embed("ยินดีต้อนรับ", f"ยินดีต้อนรับ {member.mention}!"))

@bot.event
#ออก
async def on_member_remove(member):
    channel = bot.get_channel(1120311887184277528) #IDห้อง
    await channel.send(embed=make_embed("ลาก่อน", f"ลาก่อน {member.mention}!"))
    await member.send(embed=make_embed("ลาก่อน", f"ลาก่อน {member.mention}!"))

#chat bot
@bot.event
async def on_message(message):
    mes = message.content #ดึงข้อความ
    if mes == "สวัสดี" or mes == "Hello" or mes == "hi" or mes == "Hi" or mes == "ดีครับ" or mes =="ดี" or mes == "hello":
        await message.channel.send(embed = make_embed("สวัสดี",f"สวัสดี {message.author.mention}")) #ส่งข้อความไปที่ห้อง

<<<<<<< HEAD
bot.run(get_token()) #ดึง bot token 
                     #เก็บ token ไว้ในอีกไฟล์
=======
bot.run(token)
>>>>>>> 5b40d920f92b530ead073f56dfbecf31ecfd53b3
