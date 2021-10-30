const { SlashCommandBuilder } = require('@discordjs/builders');
const EhehImageList = ['img/eh eh boi1.webp', 'img/eh eh boi2.jpg', 'img/eh eh boi3.gif', 'img/eh eh boi4.png'];
const ExcusemeImageList = ['img/excuseme.jpg', 'img/excuseme3.jpg', 'img/excuseme2.jpg'];

module.exports = {
	data: new SlashCommandBuilder()
		.setName('meme')
		.setDescription('Send the choose meme')
		.addStringOption(option =>
			option.setName('meme_name')
				.setDescription('The meme name')
				.setRequired(true)
				.addChoice('FBI', 'fbi')
				.addChoice('Police', 'police')
				.addChoice('Excuse Me Wtf', 'excusemewtf')
				.addChoice('Eh Eh Boi', 'ehehboi')),

	async execute(interaction) {
		const choice = interaction.options.getString('meme_name');
		console.log(choice);
		if (choice === 'ehehboi') {
			await interaction.reply({ files: [EhehImageList[Math.floor(Math.random() * EhehImageList.length)]] });
		} 
		else if (choice === 'excusemewtf') {
			await interaction.reply({ files: [ExcusemeImageList[Math.floor(Math.random() * ExcusemeImageList.length)]] });
		}
		else if (choice === 'fbi') {
			await interaction.reply({ files: ['./img/fbi.gif'] });
		}
		else if (choice === 'police') {
			await interaction.reply({ files: ['./img/police.jpg'] });
		}
	},
};