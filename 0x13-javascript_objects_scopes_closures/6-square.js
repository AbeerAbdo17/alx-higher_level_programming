#!/usr/bin/node
const OldSquare = require('./5-square');

class Square extends OldSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let xv = 0; xv < this.height; xv++) {
      let xrow = '';
      for (let xy = 0; xy < this.width; xy++) {
        xrow += c;
      }
      console.log(xrow);
    }
  }
}

module.exports = Square;
