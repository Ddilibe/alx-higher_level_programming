#!/usr/bin/node
exports.converter = function (base) {
	function change(jame) {
		return jame.toString(base);
	}
	return (change);
}
