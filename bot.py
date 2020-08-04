# -*- coding: utf_8 -*-

import discord, logging

import json, urllib.request
from random import choice

class MyClient(discord.Client):
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
        members = self.get_all_members()
        for m in members:
            if m.id ==memberId:
                return m
            else:
                return None

    async def sendDM(self, member, message):
        """
        Sens a dm to a member
        """
        if member.dm_channel == None:
            await member.create_dm()
        else:    
            await member.dm_channel.send(message)

    async def setrole(self, memberId, role_name):
        guild = discord.Client.get_guild(self, 622098638033780747)
        roleTD = {
            "SC": discord.utils.get(guild.roles, id=622725595976957955),
            "Eco": discord.utils.get(guild.roles, id=622725736213774347),
            "L1": discord.utils.get(guild.roles, id=738818487480483920),
            "L2": discord.utils.get(guild.roles, id=738818587292074104),
            "L3": discord.utils.get(guild.roles, id=738833214021566556),
            "Non-Miashs" : discord.utils.get(guild.roles, id=626693895421558784),
        }
        member = discord.utils.get(guild.members, id=memberId)
        await member.add_roles(roleTD[role_name])
        await self.sendDM(member, "Rôle atribué: " + str(roleTD[role_name].name))
        print("Role set for"+ member.name)
    
    async def removeRole(self, memberId, role_name):
        guild = discord.Client.get_guild(self, 622098638033780747)
        roleTD = {  
            "SC":discord.utils.get(guild.roles, id=622725595976957955),
            "Eco":discord.utils.get(guild.roles, id=622725736213774347),
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
                print("Role remove for {}".format(member.mention))
                return
        await self.sendDM(member, "Petit bug ?? t'a pas le rôle à remove, pas grave réessaye")

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
    
    async def on_member_join(self, member):
        await self.get_channel(623826045186998313).send("Yo @ {} ! Check les règles et choisis tes rôles dans #rôles".format(member.mention))
        await self.get_channel(623826045186998313).send("")

    async def on_member_remove(self, member):
        await self.get_channel(622098638033780749).send("ptdr bye {}".format(self.getMember(member.id)))
    
    async def on_raw_reaction_add(self, payload):
        one = "1⃣"
        two = "2⃣"
        three ="3⃣"
        four = "4⃣"
        five = "5⃣"
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
        one = "1⃣"
        two = "2⃣"
        three ="3⃣"
        four = "4⃣"
        five = "5⃣"
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
        print('Message from {0.author}: {0.content}'.format(message))

        #MINECRAFT
        if message.content.lower().startswith("comment va le serveur ?"):
            await message.channel.send(self.extractJson())
        
        #MEMES
        if message.content.lower().startswith("wtf"):
            imgList3= ["wtf.gif", "wtf2.gif"]
            await message.channel.send(file=discord.File(choice(imgList3)))
        #
        if message.content.lower().startswith("fbi"):
            await message.channel.send(file=discord.File("fbi.gif"))
        #
        if message.content.lower().startswith("police"):
            await message.channel.send(file=discord.File("police.jpg"))
        #
        if message.content.lower().startswith("excuse me wtf"):
            imgList1 = ["excuseme.jpg", "excuseme3.jpg","excuseme2.jpg"]
            await message.channel.send(file=discord.File(choice(imgList1)))
        #
        if message.content.lower().startswith("eh eh boi"):
            imgList = ["eh eh boi1.webp", "eh eh boi2.jpg", "eh eh boi3.gif","eh eh boi4.png", "eh eh boi5.gif"]
            await message.channel.send(file=discord.File(choice(imgList)))
        
        #UTILITY
        if message.content.lower().startswith("!help"):
            embed=discord.Embed(title="Help du bot", description="Petit appercu de ce petit bot un peu useless ", color=0xffc800)
            embed.add_field(name="memes", value="`wtf` | `fbi` | `police` | `excuse me wtf` | `eh eh boi`", inline=True)
            embed.add_field(name="Minecraft (y'a plus de serveur pour l'instant)", value="`comment va le serveur ?`", inline=False)
            embed.add_field(name="Utility", value="`salut le bot` | `!help`", inline=True)
            embed.add_field(name="Admin", value="`idtouser` | `plscleanchan` | `!mute`", inline=True)
            embed.set_footer(text="(en vrais si avez des idées de fonctionnalités je prend 🙃)")
            await message.channel.send(embed=embed)

        if message.content.lower().startswith("salut le bot"):
            await message.channel.send("Yo {} :hand_splayed:".format(message.author.mention))

        if message.content.startswith("!mute"):
            self.getMember(message.content.split(' ')[1])

        if message.content.lower().startswith("idtouser"):
            await message.channel.send(self.getMember(message.content[9:])) 

        if message.content.lower().startswith("plscleanchan"):
            #First geting which Guild(server) the message was sent, then getting the role by id 
            if discord.utils.get(discord.Client.get_guild(self, 622098638033780747).roles, id=622103979366547457) in message.author.roles:
                number = int(message.content.split(" ")[1])
                deleted = await message.channel.purge(limit=number + 1) # + the command message
                print(deleted)
                await message.channel.send(content='Deleted {} message(s)'.format(len(deleted)), delete_after=3)
            else:
                await message.channel.send("T'as pas le droit cheh")

logging.basicConfig(level=logging.DEBUG)
client = MyClient()
client.run('token')
