#!/usr/bin/node

const BaseSquare = require('./5-square'); // Import the Square class from 5-square.js

class Square extends BaseSquare {
  charPrint (c) {
    const char = c || 'X'; // Use c if provided, otherwise default to 'X'
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
}

module.exports = Square;
