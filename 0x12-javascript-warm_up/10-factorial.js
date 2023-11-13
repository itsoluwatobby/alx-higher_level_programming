#!/usr/bin/node
// a script that computes and prints a factorial
const args = require('process').argv;
function factorize (num) {
  if (num === 1) return 1;
  if (isNaN(Number(num))) return 1;
  else {
    return Number(num) * factorize(Number(num) - 1);
  }
}
const result = factorize(args[2]);
console.log(result);
