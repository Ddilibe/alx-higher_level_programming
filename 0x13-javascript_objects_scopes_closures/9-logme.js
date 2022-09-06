#!/usr/bin/node
let nu = 0;
exports.logMe = function (item) {
  console.log(`${nu}: ${item}`);
  nu = nu + 1;
};
