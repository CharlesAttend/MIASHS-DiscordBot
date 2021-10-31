const { SlashCommandBuilder } = require('@discordjs/builders');
const { colorRoleList } = require('./color.js');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('colorlist')
		.setDescription('List possible role color'),
	async execute(interaction) {
		let guildColorRoleList = interaction.guild.roles.cache
			.filter(guildRole => {
				return colorRoleList.includes(guildRole.name);
			})
			.mapValues(roleid => `${roleid}`)
			.values();
		guildColorRoleList = Array.from(guildColorRoleList);
		await interaction.reply({ content: guildColorRoleList.join(''), ephemeral: true });
	},
};