#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    // call Rectangle class
    super(size, size);
    this.size = size;
  }

  // Instance method
  charPrint (value) {
    if (!value) {
      value = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      console.log(value.repeat(this.size));
    }
  }
}
module.exports = Square;
