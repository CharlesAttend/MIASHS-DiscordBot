module.exports = {
	name: 'messageCreate',
	wtfImageList: ['./img/wtf.gif', './img/wtf2.gif'],
	async execute(message) {
		console.log('new message :', message.content);
		const content = message.content.toLowerCase();
		if (content.startsWith('wtf')) {
			await message.channel.send({ files: [this.wtfImageList[Math.floor(Math.random() * this.wtfImageList.length)]] });
		}
	},
};