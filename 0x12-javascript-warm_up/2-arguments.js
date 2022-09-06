#!/usr/bin/node
const d = process.argv;
let p = '';
if (d.length === 2) {
  p = 'No argument';
} else if (d.length === 3) {
  p = 'Argument found';
} else {
  p = 'Arguments found';
}
console.log(p);
