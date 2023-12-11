import discord
from discord.ext.commands import bot
import asyncio
import sys
#command prefix will be "+ijz0vpkNYmqru/BiUmx1w=="

prefix = "+ijz0vpkNYmqru/BiUmx1w== "
async def connect():
    reader,writer = await asyncio.open_connection("31.205.17.161",8008)
    if not reader:
        sys.exit();

async def sendCommand(command,duration,frequency):
    global ip,port,prefix
    try:
        reader,writer = await asyncio.open_connection(ip,port)
        message = prefix + command + " " + str(duration)+" "+ str(frequency)
        writer.write(message.encode())
        data = await reader.read(100)
        response = data.decode()
    except Exception as e:
        response = "-1"
    writer.close()
    await writer.wait_closed()
    if response == "-1":
        return False
    return True
        
intents = discord.Intents.all()
client = discord.Client(command_prefix="/",intents=intents)
bot = discord.ext.commands.Bot("/",intents=intents)
@bot.event
async def on_ready():
    print("online")

@bot.command(name="beep")
async def beep(ctx,duration=1,frequency=2000):
    """Sends a beep command to all connected clients.

    Arguments:
    - duration (int): Time in seconds to beep (default: 1)
    - frequency (int): Frequency to beep at (default: 2000)
    """
    result = await sendCommand("beep",duration,frequency)
    if result:
        await ctx.send("boop")
    else:
        await ctx.send("failure...")


if __name__ == "__main__":
    ip,port = "192.168.56.1",8008
    f = open("token.txt","r")
    token = f.readline()
    f.close()
    bot.run(token);