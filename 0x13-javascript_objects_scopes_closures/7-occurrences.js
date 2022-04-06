#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (const num of list) {
    if (num === searchElement) {
      counter++;
    }
  }
  return counter;
};
