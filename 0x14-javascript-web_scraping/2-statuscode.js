#!/usr/bin/node

const request = require('request');
const args = process.argv;
const URL = args[2];

request(URL, (error, response) => {
  if (error) {
    console.error('error:', error); // Print the error if one occurred
  }
  console.log('code:', response.statusCode); // Print the response status code if a response was received
});
