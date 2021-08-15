# -*- coding: utf_8 -*-

import discord, logging
import config
import json, urllib.request
from os import system
from random import choice

class MyClient(discord.Client):
    def __init__(self):
        super().__init__()
        self.mutedUser = []
    
    def extractJson(self):
        """
        Get minecraft server status from omgserv api
        """
        try:
            with urllib.request.urlopen("https://panel.omgserv.com/json/248153/status") as url:
                data = json.loads(url.read().decode())
                online = data["status"]["online"]
                cpu = str(data["status"]["cpu"]) + "%"
                ram = str(data["status"]["ram"]) + " Octet"
                version = data["status"]["version"]
                playerOnline = data["status"]["players"]["online"]
                playerMax = data["status"]["players"]["max"]
            with urllib.request.urlopen("https://panel.omgserv.com/json/248153/players") as url:
                players = json.loads(url.read().decode())["players"]
            if online:
                online = "Ouiii"
            msg = """```Status du serveur :
                    En ligne : {} 
                    Version : {}
                    CPU : {}
                    RAM : {}
                    Joueur(s) connecté(s) : {}/{} : {}```
                """.format(online, version, cpu, ram, playerOnline, playerMax, players)
            return msg
        except:
            return "`SERVER DOWN @Charles#9412"
        
    def getMember(self, memberId):
        """
        Get member by id
        """
        logger.info("getmember launched")
        members = self.get_all_members()
        for m in members:
            if m.id ==memberId:
                logger.info("Member Found")
                return m
            else:
                logger.info("Member not found")
                return None

    async def sendDM(self, member, message):
        """
        Sens a dm to a member
        """
        if member.dm_channel == None:
            await member.create_dm()
            await member.dm_channel.send(message)
        else:    
            await member.dm_channel.send(message)
        logger.info("Sended message to {} : {}".format(member.name, message))

    async def setrole(self, memberId, role_name):
        guild = discord.Client.get_guild(self, 622098638033780747)
        roleTD = {
            "SC": discord.utils.get(guild.roles, id=622725595976957955),
            "Eco": discord.utils.get(guild.roles, id=738833398096986134),
            "L1": discord.utils.get(guild.roles, id=738818487480483920),
            "L2": discord.utils.get(guild.roles, id=738818587292074104),
            "L3": discord.utils.get(guild.roles, id=738833214021566556),
            "Non-Miashs" : discord.utils.get(guild.roles, id=626693895421558784),
        }
        member = discord.utils.get(guild.members, id=memberId)
        await member.add_roles(roleTD[role_name])
        await self.sendDM(member, "Rôle atribué: {}".format(str(roleTD[role_name].name)))
        logger.info("Role set for "+ member.name)
    
    async def removeRole(self, memberId, role_name):
        guild = discord.Client.get_guild(self, 622098638033780747)
        roleTD = {  
            "SC":discord.utils.get(guild.roles, id=622725595976957955),
            "Eco":discord.utils.get(guild.roles, id=738833398096986134),
            "L1": discord.utils.get(guild.roles, id=738818487480483920),
            "L2": discord.utils.get(guild.roles, id=738818587292074104),
            "L3": discord.utils.get(guild.roles, id=738833214021566556),
            "Non-Miashs" : discord.utils.get(guild.roles, id=626693895421558784),
        }
        member = discord.utils.get(guild.members, id=memberId)
        for r in member.roles:
            if r == roleTD[role_name]:
                await member.remove_roles(roleTD[role_name])
                await self.sendDM(member, "Rôle suprimé : " + str(roleTD[role_name].name))
                logger.info("Role remove for {}".format(member.user))
                return
        await self.sendDM(member, "Petit bug, tu devais pas avoir le rôle à remove, pas grave réessaye ;)")

    async def on_ready(self):
        logger.info('Logged on as {0}!'.format(self.user))
    
    async def on_member_join(self, member):
        await self.get_channel(623826045186998313).send("Yo {} ! Check les règles et choisis tes rôles dans #rôles".format(member.mention))
        await self.get_channel(623826045186998313).send("")

    async def on_member_remove(self, member):
        await self.get_channel(622098638033780749).send("ptdr bye {}".format(member.name))
    
    async def on_raw_reaction_add(self, payload):
        one = "1️⃣"
        two = "2️⃣"
        three ="3️⃣"
        if payload.channel_id == 622456569543524352:
            if payload.message_id == 622715864722046987: #MIASH Majeur
                if payload.emoji.name == "🤔":
                    await self.setrole(payload.user_id, "SC")
                elif payload.emoji.name == "💵":
                    await self.setrole(payload.user_id, "Eco")
                elif payload.emoji.name == one:
                    await self.setrole(payload.user_id, "L1")
                elif payload.emoji.name == two:
                    await self.setrole(payload.user_id, "L2")
                elif payload.emoji.name == three:
                    await self.setrole(payload.user_id, "L3")
                elif payload.emoji.name == "🤓":
                    await self.setrole(payload.user_id, "Non-Miashs")

    async def on_raw_reaction_remove(self, payload):
        one = "1️⃣"
        two = "2️⃣"
        three ="3️⃣"
        if payload.channel_id == 622456569543524352:
            if payload.message_id == 622715864722046987: #MIASH Majeur
                if payload.emoji.name == "🤔":
                    await self.removeRole(payload.user_id, "SC")
                elif payload.emoji.name == "💵":
                    await self.removeRole(payload.user_id, "Eco")
                elif payload.emoji.name == one:
                    await self.removeRole(payload.user_id, "L1")
                elif payload.emoji.name == two:
                    await self.removeRole(payload.user_id, "L2")
                elif payload.emoji.name == three:
                    await self.removeRole(payload.user_id, "L3")
                elif payload.emoji.name == "🤓":
                    await self.removeRole(payload.user_id, "Non-Miashs")

    
    async def on_message(self, message):
        if message.author == self.user:
            return
        logger.info('Message from {0.author}: {0.content}'.format(message))
        
        #MUTE 
        if message.content.startswith("!unmute"):
            if message.author.id == 102706746392313856:
                id = message.content.split(' ')[1]
                self.mutedUser.remove(int(id))
                logger.info("Unmuted user {}".format(id))

        if message.content.startswith("!mute"):
            id = message.content.split(' ')[1]
            self.mutedUser.append(int(id))
            logger.info("Muted user {}".format(id))

        if message.author.id in self.mutedUser:
            await message.delete()
            await self.sendDM(message.author, "Tu es mute")
            logger.info("Deleted message from muted user {} with id {}".format(message.author.name, message.author.id))
        

        #MINECRAFT
        if message.content.lower().startswith("comment va le serveur ?"):
            await message.channel.send(self.extractJson())
        
        #MEMES
        if message.content.lower().startswith("wtf"):
            imgList3= ["img/wtf.gif", "img/wtf2.gif"]
            await message.channel.send(file=discord.File(choice(imgList3)))
        #
        if message.content.lower().startswith("fbi"):
            await message.channel.send(file=discord.File("img/fbi.gif"))
        #
        if message.content.lower().startswith("police"):
            await message.channel.send(file=discord.File("img/police.jpg"))
        #
        if message.content.lower().startswith("excuse me wtf"):
            imgList1 = ["img/excuseme.jpg", "img/excuseme3.jpg","img/excuseme2.jpg"]
            await message.channel.send(file=discord.File(choice(imgList1)))
        #
        if message.content.lower().startswith("eh eh boi"):
            imgList = ["img/eh eh boi1.webp", "img/eh eh boi2.jpg", "img/eh eh boi3.gif","img/eh eh boi4.png"]
            await message.channel.send(file=discord.File(choice(imgList)))
        
        #UTILITY
        if message.content.lower().startswith("!help"):
            embed=discord.Embed(title="Help du bot", description="Petit appercu de ce petit bot un peu useless (https://github.com/CharlesAttend/MIASHS-DiscordBot)", color=0xffc800)
            embed.add_field(name="memes", value="`wtf` | `fbi` | `police` | `excuse me wtf` | `eh eh boi`", inline=True)
            embed.add_field(name="Minecraft (y'a plus de serveur pour l'instant)", value="`comment va le serveur ?`", inline=False)
            embed.add_field(name="Utility", value="`salut le bot` | `!help` | `choice`", inline=True)
            embed.add_field(name="Admin", value="`idtouser` | `plscleanchan` | `!mute/!unmute + id`", inline=True)
            embed.set_footer(text="(en vrais si avez des idées de fonctionnalités je prend 🙃)")
            await message.channel.send(embed=embed)

        if message.content.lower().startswith("salut le bot"):
            await message.channel.send("Yo {} :hand_splayed:".format(message.author.mention))
        if message.content.lower().startswith("good boy"):
            await message.channel.send("Je suis le seul est unique good boy")
                
        if message.content.lower().startswith("idtouser"):
            await message.channel.send(self.getMember(message.content[9:])) 

        if message.content.lower().startswith("plscleanchan"):
            #First geting which Guild(server) the message was sent, then getting the role by id 
            if discord.utils.get(discord.Client.get_guild(self, 622098638033780747).roles, id=622103979366547457) in message.author.roles:
                number = int(message.content.split(" ")[1])
                deleted = await message.channel.purge(limit=number + 1) # + the command message
                logger.info(deleted)
                await message.channel.send(content='Deleted {} message(s)'.format(len(deleted)), delete_after=3)
            else:
                await message.channel.send("T'as pas le droit cheh")
        
        if message.content.lower().startswith("startmcserver"):
            msg = system("/home/charles/wol.sh")
            await message.channel.send(f"Command exited with status {msg}")

        if message.content.lower().startswith("choice"):
            await message.channel.send(choice(message.content.split(" ")[1:]))


logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = MyClient()
client.run(config.token)
