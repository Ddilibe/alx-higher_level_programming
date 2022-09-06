#!/usr/bin/node
module.exports = class Rectangle {
	constructor(w, h){
		if (w > 0 && h > 0) {
			this.width = w;
			this.height = h;
		}
	}

	print() {
		let X = "X";
		let a = 0;
		let b = 0;
		while (a < this.height) {
			let send = [];
			while (b < this.width) {
				send.push(X);
				b = b + 1;
			}
			b = 0;
			a = a + 1;
			console.log(send.join(''));
		}
	}

	rotate() {
		let s = this.height;
		this.height = this.width;
		this.width = s;
	}

	double() {
		this.width = this.width * 2;
		this.height = this.height * 2;
	}
}
