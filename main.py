import discord
from dotenv import load_dotenv
import os

load_dotenv()
#TOKEN de configuração do discord
TOKEN = os.getenv("TOKEN")

#Canal lido pelo Bot
canal = 'comandos-bot'

client = discord.Client()

#Status do Bot
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('!comandos'))

#Requisição e Resposta
@client.event
async def on_message(message):
    user_message = str(message.content)

    if message.author == client.user:
        return

    if message.channel.name in canal:
        if user_message.lower() == '!heróis' or user_message.lower() == '!herois':
            embed = discord.Embed(title="Nível dos Heróis por CV", description="CV10: Casal Nv40\nCV11: Casal Nv50 e Guardião Nv20\nCV12: Casal Nv65 e Guardião Nv40\nCV13: Casal Nv75, Guardião Nv50 e Campeã Nv25\nCV14: Casal Nv80, Guardião Nv55, Campeã Nv30 e Pets Nv10", color=0x351C75)
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/906288424087076944/906317899675861002/crown.png?width=461&height=461")

            await message.channel.send(embed = embed)
            return

        elif user_message.lower() == '!feitiços 8' or user_message.lower() == '!feitiços 9' or user_message.lower() == '!feiticos 8' or user_message.lower() == '!feiticos 9':
            if user_message.lower() == '!feitiços 8' or user_message.lower() == '!feiticos 8':
                embed = discord.Embed(title="Número de feitiços por defesa", description="Defesa Aérea:\n- Nv9: 3 Raios - Nv10: 3 Raios\n- Nv11: 4 Raios - Nv12: 4 Raios\n\n"
                + "Torre Inferno:\n- Nv5: 4 Raios + 1 Terremoto\n- Nv6: 5 Raios + 1 Terremoto\n- Nv7: 5 Raios + 1 Terremoto\n- Nv8: 6 Raios + 1 Terremoto\n\n"
                + "Artilharia Águia:\n- Nv2: 7 Raios + 1 Terremoto\n- Nv3: 8 Raios + 1 Terremoto\n- Nv4: 8 Raios + 1 Terremoto\n- Nv5: 9 Raios + 1 Terremoto\n\n"
                + "Disseminador:\n- Nv1: 6 Raios + 1 Terremoto\n- Nv2: 7 Raios + 1 Terremoto\n- Nv3: 8 Raios + 1 Terremoto\n\n"
                + "Cálculos feitos utilizando Raio Nv8 e Terremoto Nv5", color=0x351C75)
            else:
                embed = discord.Embed(title="Número de feitiços por defesa", description="Defesa Aérea:\n- Nv9: 3 Raios - Nv10: 3 Raios\n- Nv11: 3 Raios - Nv12: 3 Raios\n\n"
                + "Torre Inferno:\n- Nv5: 4 Raios + 1 Terremoto\n- Nv6: 4 Raios + 1 Terremoto\n- Nv7: 5 Raios + 1 Terremoto\n- Nv8: 5 Raios + 1 Terremoto\n\n"
                + "Artilharia Águia:\n- Nv2: 6 Raios + 1 Terremoto\n- Nv3: 7 Raios + 1 Terremoto\n- Nv4: 7 Raios + 1 Terremoto\n- Nv5: 8 Raios + 1 Terremoto\n\n"
                + "Disseminador:\n- Nv1: 5 Raios + 1 Terremoto\n- Nv2: 6 Raios + 1 Terremoto\n- Nv3: 7 Raios + 1 Terremoto\n\n"
                + "Cálculos feitos utilizando Raio Nv9 e Terremoto Nv5", color=0x351C75)
            
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/906735573241319435/906756781622063144/potion_2.png")
            await message.channel.send(embed = embed)
            return

        elif user_message.lower() == '!comandos':
            embed = discord.Embed(title="Comandos", description=f"!heróis - Mostra o nível máximo dos heróis por CV\n!feitiços N - Mostra a quantidade de feitiços para destruir uma defesa\n- N = nível do raio\n- 0 bot aceita N = 8 ou 9", color=0x351C75)
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/906288424087076944/906326438083444756/web-management.png?width=461&height=461")

            await message.channel.send(embed = embed)
            return

        else:
            return

client.run(TOKEN)