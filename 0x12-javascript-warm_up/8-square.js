#!/usr/bin/node
// a script that prints a square
const args = require('process').argv;
let response = '';
if (isNaN(Number(args[2]))) console.log('Missing size');
else {
  for (let i = 0; i < Number(args[2]); i++) {
    for (let i = 0; i < Number(args[2]); i++) {
      response += 'x';
    }
    console.log(response);
    response = '';
  }
}
