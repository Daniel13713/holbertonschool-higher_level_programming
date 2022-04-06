#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    // call Rectangle class
    super(size, size);
  }
}
module.exports = Square;
