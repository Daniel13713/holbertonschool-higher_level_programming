#!/usr/bin/node

const request = require('request');
const args = process.argv;

const URL = 'https://swapi-api.hbtn.io/api/films/' + args[2];

request.get(URL, (error, response, body) => {
  if (error) {
    console.error('error:', error);
  }
  const data = JSON.parse(body);
  console.log(data.title);
});
