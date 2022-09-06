#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');

module.exports = class Square extends Rectangle {
	constructor (size) {
		super(size, size);
		this.size = size;
	}

	charPrint(c) {
		if (c) {
			let X = c;
			let a = 0;
			while (a < this.size) {
				let send = [];
				let b = 0;
				while (b < this.size) {
					send.push(X);
					b = b + 1;
				}
				console.log(send.join(''));
				a = a + 1;
			}
		} else {
			super.print();
		}
	}
}
