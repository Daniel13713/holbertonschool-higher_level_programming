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

  const arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  const isCompleted = (user) => user.completed;
  const usersCompleted = data.filter(isCompleted);
  const forId = arr.map((id) => {
    return usersCompleted.filter((user) => {
      return user.userId === id;
    }).length;
  }).reduce((total, value, index) => {
    return {
      ...total,
      [index + 1]: value
    };
  }, {});
  console.log(JSON.stringify(forId));
});
