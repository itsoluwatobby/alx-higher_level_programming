#!/usr/bin/node
const args = require('process').argv;
if (isNaN(Number(args[2]))) console.log('Missing size');
else {
  for (let i = 0; i < Number(args[2]); i++) {
    let response = '';
    for (let j = 0; j < Number(args[2]); j++) response += 'x';
    console.log(response);
  }
}
