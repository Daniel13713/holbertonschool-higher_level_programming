#!/usr/bin/node

const file = require('fs');
const args = process.argv;

const data1 = file.readFileSync(args[2], 'utf8');
const data2 = file.readFileSync(args[3], 'utf8');
file.writeFileSync(args[4], data1 + data2);
