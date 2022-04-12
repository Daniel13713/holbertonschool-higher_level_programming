#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const args = process.argv;

const URL = args[2];
const File = args[3];

request.get(URL, (error, response, body) => {
  if (error) {
    /* Print the error if one occurred */
    console.error('error:', error);
  }
  fs.writeFile(File, body, { flag: 'a' }, err => {
    if (err) {
      console.log(err);
    }
    /* Written fine */
  });
});
