#!/usr/bin/node
function add (a, b) {
  return (Number.parseInt(a) + Number.parseInt(b));
}
const james = process.argv;
console.log(add(james[2], james[3]));
