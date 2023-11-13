#!/usr/bin/node
// a script that prints the addition of 2 integers
const args = require('process').argv;
if (isNaN(Number(args[2])) || isNaN(Number(args[3]))) console.log('NaN');
else console.log(Number(args[2]) + Number(args[3]));
