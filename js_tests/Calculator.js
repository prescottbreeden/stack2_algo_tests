'use strict'

module.exports = class Calculator {
  constructor() {
    this.total = 0;
  }

  add(num) { this.total += num } 
  subtract(num) { this.total -= num }
  multiply(num) { this.total *= num }
  divide(num) { this.total /= num }
}
