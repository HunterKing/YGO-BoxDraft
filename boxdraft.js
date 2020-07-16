const fetch = require('node-fetch');
const http = require('http');
const fs = require('fs');
const file = './data.json'

if(!fs.existsSync(file)){
	console.log("Creating Data File...");
	fetch('https://db.ygoprodeck.com/api/v7/cardinfo.php')
		.then(res => res.json())
		.then(json => {
			let fullData = JSON.stringify(json);
			fs.writeFileSync(file, fullData);	
		});
	const data = require './data.json'
};
else{
	const data = require './data.json'
}

