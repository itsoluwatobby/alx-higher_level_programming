#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (!c) this.print();
    else {
      for (let i = 0; i < this.height; i++) {
        let res = '';
        for (let j = 0; j < this.height; j++) res += c;
        console.log(res);
      }
    }
  }
};
