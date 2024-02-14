#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print() {
    for (let i = 0; i < h; i++) {
      for (let j = 0; j < w; j++) {
        console.log('X');
      }
      console.log();
    }
  }
};
