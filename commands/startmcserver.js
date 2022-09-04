const { SlashCommandBuilder } = require('@discordjs/builders');
const { MessageActionRow, MessageButton, MessageEmbed } = require('discord.js');
// const { NodeSSH } = require('node-ssh');
// require('dotenv').config();

// const ssh = new NodeSSH();
// const login = {
// 	host: process.env.IP_ADDRESS,
// 	username: process.env.USERNAME,
// 	password: process.env.PASSWORD,
// };

const { exec } = require("child_process");


const row = new MessageActionRow()
	.addComponents(
		new MessageButton()
			.setCustomId('shutdown')
			// eslint-disable-next-line quotes
			.setLabel("J'ai éteint l'ordi ;)")
			.setStyle('PRIMARY')
			.setEmoji('✔️'),
	);
const filter = i => {
	i.deferUpdate();
	return i.customId === 'shutdown';
};

module.exports = {
	data: new SlashCommandBuilder()
		.setName('startmcserver')
		.setDescription('Allumer le serveur Minecraft'),
	async execute(interaction) {
		try {
			// Serveur de l'élite or I'm gay
			if (interaction.guildId === '697903202586067035' || interaction.guildId === '459801881296764928') {
				await interaction.reply('Démarrage en cours...');
				// await ssh.connect(login);
				// const { stdout, stderr } = await ssh.execCommand('./wol.sh');
				// console.log(stderr + '\n', stdout);
				exec('~/wol.sh', (error, stdout, stderr) => {
					// catch err, stdout, stderr
					if (error) {
						console.log('Error in wol.sh:', error);
						return;
					}
					else if (stderr) {
						console.log('an error with file system during wol:', stderr);
						return;
					}
					else {
						console.log('Result of shell script execution:', stdout);
					}
				});
				const message = await interaction.editReply({ content: 'Packet WOL envoyé ! Pensez à éteindre mon ordinateur via Parsec une fois terminé ;)', components: [row], fetchReply: true });
				await message.awaitMessageComponent({ filter, time: 60000, componentType: 'BUTTON' });
				await interaction.editReply({ content: 'Merci beaucoup !!!', components: [] });
			}
			else {
				// eslint-disable-next-line quotes
				await interaction.reply({ content: "Cette commande n'est pas pour toi ;)", ephemeral: true });
			}
		}
		catch (error) {
			console.log(error);
		}
	},
};
