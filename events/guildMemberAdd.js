const { MessageEmbed } = require('discord.js');

module.exports = {
	name: 'guildMemberAdd',
	async execute(member) {
		console.log('New member');
		const welcomeMessage = new MessageEmbed()
			.setTitle(`Bienvenu ${member.displayName} !`)
			.setColor(Math.floor(Math.random() * 16777215).toString(16))
			.setDescription('Choisis tes rôles avec la commande **/roles** !')
			.setFooter('Discord de la Licence MIASHS')
			.setThumbnail(member.user.avatarURL({ size: 1024 }))
			.setAuthor(member.client.user.username, member.client.user.displayAvatarURL(), 'https://github.com/CharlesAttend/MIASHS-DiscordBot/')
			.setTimestamp();

		try {
			const channel = await member.guild.channels.fetch('623826045186998313');
			// debug dans i'm gay:
			// const channel = await member.guild.channels.fetch('459804994267381760');
			await channel.send({ content: `${member}`, embeds: [welcomeMessage] });
		}
		catch(err) {
			return 0;
		}
	},
};