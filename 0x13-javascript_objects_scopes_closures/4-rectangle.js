#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w === 0 || w < 0 || !w) || (h === 0 || h < 0 || !h)) return null;
    else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let result = '';
      for (let j = 0; j < this.width; j++) result += 'X';
      console.log(result);
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
