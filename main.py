# ----------main.py for Washino Bot-----------



# ---Standard libraries---
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv(dotenv_path="config")

default_intents = discord.Intents.default()
default_intents.members = True
bot = commands.Bot(command_prefix='|', description="Washino Bot", intents=default_intents)

# ---description du bot---


@bot.event
async def on_ready():
    print(bot.user.name + " it's ready.")  # -> (Pour engistrer les messages)

    await bot.change_presence(status=discord.Status.do_not_disturb,
                              activity=discord.Activity(type=discord.ActivityType.playing,
                                                        name="Unity 2020.3.31f1 (64-bit)"), )


# ----On_message----





@bot.event
async def on_message(message):
    print(message.content)

    # ---Commande---

    # |supp
    if message.content.startswith("|supp"):
        number = int(message.content.split()[1])
        messages = await message.channel.history(limit=number + 1).flatten()

        for each_message in messages:
            await each_message.delete()

    #--Commande Basique--

    # |command
    if message.content.startswith("|command"):
        await message.channel.send("**Les commandes de Washino Bot :**"
                                   "\n"
                                   "\n"
                                   "\n|command ➜ Cette comande que vous venez d'utiliser vous permet de connaitre "
                                   "toutes les commandes disponibles "
                                   "\n"
                                   "\n|supp 1 ➜ Permet de supprimer un message ou plus par rapport au chiffre que"
                                   "vous indiquez"
                                   "\n"
                                   "\n|resaux ➜ pour avoir le lien des résaux de Washino")

    # |resaux
    if message.content.startswith("|resaux"):
        await message.channel.send("**Les Résaux de Washino :**"
                                   "\n"
                                   "\n"
                                   "\nInstagram : https://www.instagram.com/washino.studio/"
                                   "\n"
                                   "\nTwitter : https://twitter.com/StudioWashino (attente de personne pour le gérer)"
                                   "\n"
                                   "\nYoutube : Soon (attente de personne pour le gérer)")

    # |sushi
    if message.content.startswith("|sushi"):
        await message.channel.send("Gnum Gnum!")

    #|bug
    if message.content.startswith("|bug"):
        await message.channel.send("|bug")

    # --Commande Admin--

    # |paramètre

    if message.content.startswith("|parametre"):
        await message.channel.send("**Voici les commandes qu'un admin peu executer :**"
        "\n |enter : pour programmer le salon et les messages à l'arrivé d'un membre sur votre serveur."
        "\n |leave : pour programmer le salon et les messages du départ d'un membre sur votre serveur.")

    # |enter

    if message.content.startswith("|enter"):
        await message.channel.send("Veuillez rentrez l'ID du salon d'arrivé de vos membre s'il vous plait.")
        reponseEnter = int(message.content.split())
        await reponseEnter.send(content=f"Bravo, vous avez finie de programmer l'arrivée des membres tout marche à la perfection !")
        

    # |leave
    
    if message.content.startswith("|leave"):
        await message.channel.send("Veuillez rentrez l'ID du salon de départ de vos membre s'il vous plait.")
        reponseLeave = int (message.content.split())
        


    # ---Discution Bot/User---
    


    # --Français--

    # -Salut/Ca va-

    if message.content.lower() == ("bien" or "Bien"):
        await message.channel.send("Tant mieux,"
                                   "\n Je vais aller travailler..."
                                   "\n A bientôt !")

    if message.content.lower() == ("bien et toi" or "Bien Et Toi" or "Bien et Toi" or "Bien Et toi" or "Bien Et toi"):
        await message.channel.send("Bien,"
                                   "\n Je vais aller travailler..."
                                   "\n A bientôt !")

    if message.content.lower() == ("bien et vous" or "Bien Et Vous" or "Bien et Vous" or "Bien Et vous" or "Bien Et vous"):
        await message.channel.send("Bien,"
                                   "\n Je vais aller travailler..."
                                   "\n A bientôt !")

    if message.content.lower() == ("salut" or "Salut"):
        await message.channel.send("Bonjour,"
                                   "\n Comment allez-vous ?")

    if message.content.lower() == ("bonjour" or "Bonjour"):
        await message.channel.send("Bonjour,"
                                   "\n Comment aller-vous ?")


    # --Espanol--

    # -Salut/Ca va-


    if message.content.lower() == ("hola" or "Hola"):
        await message.channel.send("Hola,"
                                   "\n¿Como esta?")

    if message.content.lower() == ("Buenos dias" or "Buenos Dias" or "buenos dias" or "buenos Dias"):
        await message.channel.send("¡Buenos dias!,"
                                   "\n¿Como esta?")

    if message.content.lower() == ("muy bien" or "Muy bien" or "Muy Bien" or "muy Bien"):
        await message.channel.send("Bien,"
                                   "\nVoy a trabajar. "
                                   "\n¡Asta pronto!")

    if message.content.lower() == ("muy bien y Tú" or "Muy bien Y Tú" or "Muy Bien" or "muy Bien y Tú" or "Muy Bien y Tú"):
        await message.channel.send("Bien,"
                                "\nVoy a trabajar. "
                                "\n¡Asta pronto!")


    # --English--

    # -Salut/Ca va-


    if message.content.lower() == ("hi" or "Hi"):
        await message.channel.send("Hello,"
                                   "\nHow are you ?")

    if message.content.lower() == ("hello" or "Hello"):
        await message.channel.send("Hello,"
                                   "\nHow are you ?")

    if message.content.lower() == ("good and you" or "Good And You" or "Good and you" or "Good And You" or "Good And you" or "Good and You"):
        await message.channel.send("Good,"
                                   "\nI'm going to work ..."
                                   "\nGoodbye !")

    if message.content.lower() == ("good" or "Good"):
        await message.channel.send("Good,"
                                   "\nI'm going to work ..."
                                   "\nGoodbye !")

    # ---Respect---

        if message.content.lower() == ("feur" or "Feur"):
            await message.channel.send("Ce n'est pas de l'humour, merci de réfléchir avant d'écrire//♥♦♣♠\\")

    # --Compteur Automatique--

    if message.content.lower("|compteur"):
        numbers =  int(message.content.split()[1])
        await message.channel.send(numbers + 1)
    
# ---Réagir à l'arrivé d'un membre---


@bot.event
async def on_member_join(member):
    # Réaction arrivé (1)
    general_channel1: discord.TextChannel = bot.get_channel(830867474597150730)
    await general_channel1.send(content=f"Bienvenue {member.mention},                "
                                        f"\n                                                "
                                        f"\nBienvenue dans le serveur de Washino Studio !   "
                                        f"\n                                                "
                                        f"\nN'oubliez pas d'allez valider le règlement !")

    # Réaction arrivé (2)
    general_channel2: discord.TextChannel = bot.get_channel(830867424483082240)
    await general_channel2.send(content=f" Acceuillez comme il le faut, {member.mention}! :tada:  ")
	
    # Add role arrivé

    role_communaute = discord.utils.get(member.guild.roles, name='Communauté')
    await member.add_roles(role_communaute)

# ---Réagir au départ d'un membre---


@bot.event
async def on_member_remove(member):
    # Réaction Départ (1)
    general_channel3: discord.TextChannel = bot.get_channel(830867510999121970)
    await general_channel3.send(content=f"Aurevoir {member.mention},                "
                                        f"\n                                                "
                                        f"\n {member.mention} vien de partir du serveur de Washino Studio !   "
                                        f"\n                                                "
                                        f"\nÀ bientôt ...   ")


# ---Rôle/Réaction---


@bot.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 959850163441107035:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, bot.guilds)

        # --Rôle Event--
        if payload.emoji.name == '🎉':
            print('1 Nouveau Rôle event')
            role = discord.utils.get(guild.roles, name='Event')
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:
            member = payload.member
            if member is not None:
                await member.add_roles(role)
                print("Accepter")
            else:
                print("member not found")
        else:
            print("role not found")

        # --Rôle Annonce--

        if payload.emoji.name == '🔔':
            print('1 Nouveau Rôle annonce')
            role = discord.utils.get(guild.roles, name='Annonce')
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:
            member = payload.member
            if member is not None:
                await member.add_roles(role)
                print("Accepter")
            else:
                print("member not found")
        else:
            print("role not found")

            # --Rôle Partenariat--

            if payload.emoji.name == '🤝':
                print('1 Nouveau Rôle partenariat')
                role = discord.utils.get(guild.roles, name='Partenariat')
            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)

            if role is not None:    
                member = payload.member
                if member is not None:
                    await member.add_roles(role)
                    print("Accepter")
                else:
                    print("member not found")
            else:
                print("role not found")

                # --Rôle Journal--

                if payload.emoji.name == '🗞️':
                    print('1 Nouveau Rôle journal')
                    role = discord.utils.get(guild.roles, name='Journal')
                else:
                    role = discord.utils.get(guild.roles, name=payload.emoji.name)

                if role is not None:
                    member = payload.member
                    if member is not None:
                        await member.add_roles(role)
                        print("Accepter")
                    else:
                        print("member not found")
                else:
                    print("role not found")


# ---Warning---

@commands.has_permissions(kick_members=True)
async def warn(ctx, member: discord.Member, *, arg):
    logsChannel = bot.get_channel(829643122173673503)
    user = member.mention
    embed = discord.Embed(title="Warning issued: ", color=0xf40000)
    embed.add_field(name="Warning: ", value=f'Reason: {arg}', inline=False)
    embed.add_field(name="User warned: ", value=f'{member.mention}', inline=False)
    embed.add_field(name="Warned by: ", value=f'{ctx.author}', inline=False)
    
    embed2 = discord.Embed(title="Warning issued: ", color=0xf40000)
    embed2.add_field(name="Warning: ", value=f'Reason: {arg}', inline=False)
    embed2.add_field(name="User warned: ", value=f'{member.mention}', inline=False)
    embed2.add_field(name="Warned by: ", value=f'{ctx.author}', inline=False)
    
    await logsChannel.send(embed=embed2)
    await member.send(f'You have been warned in Jackkkks Society for **{arg}**!')
    message = await ctx.send(embed=embed)

# ---Kick---

@bot.command
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User {member} has been kicked from the server.')

bot.run(os.getenv('TOKEN'))
