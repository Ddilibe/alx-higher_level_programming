#!/usr/bin/env node
const list = require('./100-data.js').list;
const jan = list.map((j, k) => { return j * k;});
console.log(list);
console.log(jan);
