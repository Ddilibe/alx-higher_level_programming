#!/usr/bin/node
const jame = Number.parseInt(process.argv[2]);
if (jame) {
  console.log('My number: ' + jame);
} else {
  console.log('Not a number');
}
