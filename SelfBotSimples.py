from discord.ext import commands
import time

prefix = "prefixo aqui"
token = "token aqui"
bot = commands.Bot(command_prefix=prefix, self_bot=True)
count = 0

@bot.event
async def on_connect():
    print("Estou online! {bot.user.name}#{bot.user.discriminator}")


@bot.command()
async def massdm(ctx, *, message):
    global count
    await ctx.message.delete()
    members = ctx.guild.members
    for member in members:
        try:
            time.sleep(1.5)
            await member.send(message)
            count += 1
            print(f"{count} | Sucesso ao enviar a mensagem para: {member.name}#{member.discriminator}")
        except:
            print(f"Erro ao enviar mensagem para: | {member.name}#{member.discriminator}")


bot.run(token, bot=False)