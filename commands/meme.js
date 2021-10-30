const { SlashCommandBuilder } = require('@discordjs/builders');
const EhehImageList = ['img/eh eh boi1.webp', 'img/eh eh boi2.jpg', 'img/eh eh boi3.gif', 'img/eh eh boi4.png'];
const ExcusemeImageList = ['img/excuseme.jpg', 'img/excuseme3.jpg', 'img/excuseme2.jpg'];
module.exports = {
	data: new SlashCommandBuilder()
		.setName('meme')
		.setDescription('Send the choose meme')
		.addSubcommand(subcommand =>
			subcommand
				.setName('fbi')
				.setDescription('Send `FBI` meme'))
		.addSubcommand(subcommand =>
			subcommand
				.setName('police')
				.setDescription('Send `police` meme (private joke 2019 de sorry)'))
		.addSubcommand(subcommand =>
			subcommand
				.setName('excusemewtf')
				.setDescription('Send `Excuse me WTF` meme'))
		.addSubcommand(subcommand =>
			subcommand
				.setName('ehehboi')
				.setDescription('Send eh eh boi meme')),
	async execute(interaction) {
		if (interaction.options.getSubcommand() === 'ehehboi') {
			await interaction.reply({ files: [EhehImageList[Math.floor(Math.random() * EhehImageList.length)]] });
		} else if (interaction.options.getSubcommand() === 'excusemewtf') {
			await interaction.reply({ files: [ExcusemeImageList[Math.floor(Math.random() * ExcusemeImageList.length)]] });
		}
		else if (interaction.options.getSubcommand() === 'fbi') {
			await interaction.reply({ files: ['./img/fbi.gif'] });
		}
		else if (interaction.options.getSubcommand() === 'police') {
			await interaction.reply({ files: ['./img/police.jpg'] });
		}
	},
};