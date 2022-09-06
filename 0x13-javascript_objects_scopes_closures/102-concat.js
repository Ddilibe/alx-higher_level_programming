#!/usr/bin/node
const jame = process.argv;
const fs = require('fs');
const first = fs.readFileSync(jame[2], 'utf8');
const second = fs.readFileSync(jame[3], 'utf8');
const j = first + second;
try {
  fs.writeFileSync(jame[4], j);
} catch (err) {
  console.error(err);
}
