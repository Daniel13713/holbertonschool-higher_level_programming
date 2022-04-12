#!/usr/bin/node

const request = require('request');
const args = process.argv;

const URL = args[2];

request.get(URL, (error, response, body) => {
  if (error) {
    /* Print the error if one occurred */
    console.error('error:', error);
  }
  const data = JSON.parse(body);

  const result = data.results.map((film) => {
    /* return only character arrays */
    return film.characters;
  }).filter((people) => {
    for (let i = 0; people[i]; i++) {
      /* filter by id 18 */
      if (people[i] === 'https://swapi-api.hbtn.io/api/people/18/') {
        return people;
      }
    }
    return 0;
  }).length; // count the array's elements
  console.log(result);
});
