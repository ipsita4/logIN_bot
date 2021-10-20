import discord
from discord import member
from discord import message
from discord import embeds
import discord.ext.commands as commands
import os
import random
import dotenv
from dotenv import load_dotenv


load_dotenv()
client=discord.Client()

@client.event
async def on_message(message):
    greetings = ["CSAI","CSE","ECAI","ECE","IT","MAE","EEE","CE","2024","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021","2022","2023","2024","2025","2026","2027","2028","2029","2030","2031","2032","2033","2034","2035","2036","2037","2038","2039","2040","2041","2042","2043","2044","2045","2046","2047","2048","2049","2050","2051","2052","2053","2054","2055","2056","2057","2058"]


    if message.author.bot: return
    if any(word in message.content.lower()for word in greetings):
        if message.author == client.user:
            return
    
    else:
        await message.channel.send("Hello there, your attendence is not verified, " + str(message.author))
        
        return
    await message.channel.send("Hello there,your attendence is verified " + str(message.author))
    print("Reply to hello command has been executed")




@client.event

async def on_ready():
    generel_channel= client.get_channel(882930150667329541)

    await generel_channel.send('hello')



client.run(os.getenv('TOKEN'))
