const { SlashCommandBuilder } = require('@discordjs/builders');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('choices')
		.setDescription('Pick a random choice from list')
		.addStringOption(option =>
			option.setName('input')
				.setDescription('Enter each choice separated by a space')
				.setRequired(true)),
	async execute(interaction) {
		const choiceList = interaction.options.getString('choices').split(' ');
		await interaction.reply(choiceList[Math.floor(Math.random() * choiceList.length)]);
	},
};