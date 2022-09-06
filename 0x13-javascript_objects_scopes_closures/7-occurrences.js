#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
	let r = 0;
	for (let jame of list) {
		if (jame === searchElement)
			r = r + 1;
	}
	return r;
}
