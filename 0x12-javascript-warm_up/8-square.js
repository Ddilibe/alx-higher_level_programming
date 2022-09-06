#!/usr/bin/node
const h = process.argv[2];
let jane = [];
if (!h) { console.log('Missing size'); }
const man = 'X';
let james = 1;
let dude = 1;
while (dude <= h) {
  james = 0;
  jane = [];
  while (james <= h) {
    jane.push(man);
    james = james + 1;
  }
  console.log(jane.join(''));
  dude = dude + 1;
}
