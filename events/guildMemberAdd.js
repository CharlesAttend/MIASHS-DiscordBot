module.exports = {
	name: 'guildMemberAdd',
	async execute(member) {
		console.log('New member');
		const channel = member.client.channels.cache.get('459804994267381760');
		const welcomeMessage = `Bienvenu ${member.id} !`;
		await channel.send(welcomeMessage);
	},
};