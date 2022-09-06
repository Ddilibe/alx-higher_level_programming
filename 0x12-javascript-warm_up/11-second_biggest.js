#!/usr/bin/node
const tube = process.argv;
const man = tube.length - 2;
if (man === 0 || man === 1)
	console.log(0);
else {
	d = 0;
	let dan = [];
	while (d < man) {
		dan.push(tube[d+2]);
		d = d + 1;
	}
	dan = dan.sort()
	dan = dan.reverse()
	console.log(dan[1]);
}
