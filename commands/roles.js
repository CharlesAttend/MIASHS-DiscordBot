const { SlashCommandBuilder } = require('@discordjs/builders');
const { MessageActionRow, MessageSelectMenu, Collection } = require('discord.js');

const YearsRow = new MessageActionRow()
	.addComponents(
		new MessageSelectMenu()
			.setCustomId('yearsSelect')
			.setPlaceholder('Sélectionne une année')
			.addOptions([
				{
					label: '1️⃣ Première Année',
					description: '',
					value: 'L1',
				},
				{
					label: '2️⃣ Deuxième Année',
					description: '',
					value: 'L2',
				},
				{
					label: '3️⃣ Troisième Année',
					description: '',
					value: 'L3',
				},
			]),
	);
const OptionRow = new MessageActionRow()
	.addComponents(
		new MessageSelectMenu()
			.setCustomId('optionSelect')
			.setPlaceholder('Sélectionne un parcourt')
			.addOptions([
				{
					label: '💵 Économie',
					description: '',
					value: 'Eco',
				},
				{
					label: '🧠 Science Cognitive',
					description: '',
					value: 'SC',
				},
				{
					label: '🖥️ MSID',
					description: '',
					value: 'MSID',
				},
				{
					label: '🤓 Non MIASHS',
					description: '(tkt on accepte tout le monde)',
					value: 'Non-Miashs',
				},
			]),
	);


const setRole = async (interaction, years, option) => {
	const roles = {
		// 'SC': await interaction.guild.roles.fetch('622725595976957955'),
		// 'Eco': await interaction.guild.roles.fetch('738833398096986134'),
		// 'MSID' : await interaction.guild.roles.fetch('626693895421558784'),
		// 'Non-Miashs' : await interaction.guild.roles.fetch('626693895421558784'),
		// 'L1': await interaction.guild.roles.fetch('738818487480483920'),
		// 'L2': await interaction.guild.roles.fetch('738818587292074104'),
		// 'L3': await interaction.guild.roles.fetch('738833214021566556'),
		'L1': await interaction.guild.roles.fetch('459809474371125250'),
		'eco':await interaction.guild.roles.fetch('738854612294959144'),
	};
	await interaction.member.roles.remove(Object.values(roles));
	await interaction.member.roles.add([roles[years], roles[option]]);
};

module.exports = {
	data : new SlashCommandBuilder()
		.setName('roles')
		.setDescription('Choisir ses rôles !'),
	async execute(interaction) {
		const filter = i => {
			i.deferUpdate();
			return i.user.id === interaction.user.id;
		};
		// asking current years and waiting for reply 
		const message = await interaction.reply({ content: 'Choisie ton années !', ephemeral: true, components: [YearsRow], fetchReply: true });
		const years = await message.awaitMessageComponent({ filter, componentType: 'SELECT_MENU', time: 60000 });
		// asking option and waiting for reply
		await interaction.editReply({ content: 'Choisie ton parcourt !', ephemeral: false, components: [OptionRow] });
		const option = await message.awaitMessageComponent({ filter, componentType: 'SELECT_MENU', time: 60000 });
		// setting roles
		await setRole(interaction, years.values, option.values);
		// validating
		await interaction.editReply({ content: 'Tes rôles ont été actualisé', ephemeral: false, components: [OptionRow] });
	},
};