#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (!c) c = 'X';
    for (let i = 0; i < this.size; i++) {
      let result = '';
      for (let j = 0; j < this.size; j++) result += c;
      console.log(result);
    }
  }
}

module.exports = Square;
