const { SlashCommandBuilder } = require('@discordjs/builders');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('choose')
		.setDescription('Pick a random choice from list')
		.addStringOption(option =>
			option.setName('choices')
				.setDescription('Enter each choice separated by a space')
				.setRequired(true))
		.addBooleanOption(option =>
			option.setName('hide')
				.setDescription('Reply in an ephemeral message')),

	async execute(interaction) {
		const choiceList = interaction.options.getString('choices').split(' ');
		await interaction.reply({ content: choiceList[Math.floor(Math.random() * choiceList.length)], ephemeral: interaction.options.getBoolean('hide') });
	},
};