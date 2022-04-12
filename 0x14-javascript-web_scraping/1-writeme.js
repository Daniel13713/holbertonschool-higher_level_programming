#!/usr/bin/node

const fs = require('fs');

const args = process.argv;
const file = './' + args[2];
const content = args[3];
fs.writeFile(file, content, { flag: 'a' }, err => {
  if (err) {
    console.log(err);
    return;
  }
  /* Written fine */
});
