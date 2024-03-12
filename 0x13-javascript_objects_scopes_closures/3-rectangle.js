#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let xv = 0; xv < this.height; xv++) {
      let xrow = '';
      for (let xy = 0; xy < this.width; xy++) {
        xrow += 'X';
      }
      console.log(xrow);
    }
  }
}

module.exports = Rectangle;
