#!/usr/bin/node
exports.converter = function (base) {
  // how works this?
  return (num) => { return num.toString(base); };
};
