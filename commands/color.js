const { SlashCommandBuilder } = require('@discordjs/builders');
const colorRoleList = ['Vert++', 'Vert', 'Bleu', 'Violet', 'Coco', 'Jaune', 'Orange', 'Orange2', 'Gris', 'Gris++', 'Rose'];

const setRole = async (interaction, role) => {
	const userRoleList = await interaction.member.roles.cache
		.filter(userRole => colorRoleList.includes(userRole.name));
	await interaction.member.roles.remove(userRoleList);
	await interaction.member.roles.add(role);
};

module.exports = {
	data: new SlashCommandBuilder()
		.setName('color')
		.setDescription('Choose a color !')
		.addRoleOption(option =>
			option
				.setName('color_role')
				.setDescription('Pick a color role')
				.setRequired(true)),
	async execute(interaction) {
		const role = interaction.options.getRole('color_role');
		if (colorRoleList.includes(role.name)) {
			await interaction.reply({ content: 'Painting a role for you 🖌️', ephemeral: true });
			await setRole(interaction, role);
			await interaction.editReply({ content: 'Brand new colors applied ✨' });
		}
		else {
			await interaction.reply({ content: 'Wrong role chosen, please only pick a color role ❎', ephemeral: true });
		}
	},
};