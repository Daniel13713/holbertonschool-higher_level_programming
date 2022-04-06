#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      /* Empty object */
    } else {
      this.width = w;
      this.height = h;
    }
  }

  // instace method
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  // exchanges width and height values
  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  // double multiply width and height by 2
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
