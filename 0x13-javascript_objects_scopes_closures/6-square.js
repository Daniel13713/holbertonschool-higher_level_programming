#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    // call Rectangle class
    super(size, size);
  }

  // Instance method
  charPrint (value) {
    if (!value) {
      value = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(value.repeat(this.width));
    }
  }
}
module.exports = Square;
