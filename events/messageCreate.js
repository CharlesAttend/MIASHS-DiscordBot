const wtfImageList = ['./img/wtf.gif', './img/wtf2.gif'];

module.exports = {
	name: 'messageCreate',
	async execute(message) {
		console.log('new message :', message.content);
		const content = message.content.toLowerCase();
		if (content.startsWith('wtf')) {
			await message.channel.send({ files: [wtfImageList[Math.floor(Math.random() * wtfImageList.length)]] });
		}
	},
};