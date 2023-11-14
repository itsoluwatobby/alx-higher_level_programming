#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w === 0 || w < 0 || !w) || (h === 0 || h < 0 || !h)) return null;
    else {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
