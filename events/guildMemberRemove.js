const { MessageEmbed } = require('discord.js');

module.exports = {
	name: 'guildMemberRemove',
	async execute(member) {
		console.log('Removed member');
		const goodbyeMessage = new MessageEmbed()
			.setTitle(`Goodbye ${member.user.username} 😔`)
			.setColor(Math.floor(Math.random() * 16777215).toString(16))
			.setDescription('Nous avons encore perdu un soldat...')
			.setFooter('Discord de la Licence MIASHS')
			.setThumbnail(member.user.avatarURL({ size: 1024 }))
			.setAuthor(member.client.user.username, member.client.user.displayAvatarURL(), 'https://github.com/CharlesAttend/MIASHS-DiscordBot/')
			.setTimestamp();
		const channel = await member.guild.channels.fetch('623826045186998313');

		// debug :
		// const channel = await member.guild.channels.fetch('459804994267381760');
		await channel.send({ embeds: [goodbyeMessage] });
	},
};