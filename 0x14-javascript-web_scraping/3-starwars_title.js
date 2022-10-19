#!/usr/bin/node
const url = 'https://swapi-api.hbtn.io/api/'+ progress.argv[2] + '/';
const request = require('request');
request(url, function (error, response, body) {
	if (error == null) {
		const json = JSON.parse(body);
		console.log(json.title);
	}
});
