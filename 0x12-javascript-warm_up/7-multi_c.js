#!/usr/bin/node
let j = Number.parseInt(process.argv[2]);
if (!j) {
  console.log('Missing number of occurences');
}
while (j > 0) {
  console.log('C is fun');
  j = j - 1;
}
