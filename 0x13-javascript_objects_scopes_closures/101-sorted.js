#!/usr/bin/node
const dict = require('./101-data.js').dict;
const ocurrences = Object.keys(dict);
const id = [...new Set(Object.values(dict))];
const new_dict = {};
for (const key of id) {
  new_dict[key] = ocurrences.filter((e) => dict[e] === key);
}
console.log(new_dict);
