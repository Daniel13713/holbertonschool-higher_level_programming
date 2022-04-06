#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const count = {};
  for (const num of list) {
    count[num] = count[num] ? count[num] + 1 : 1;
  }
  return count[searchElement];
};
