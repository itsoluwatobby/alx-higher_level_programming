#!/usr/bin/node
/**
 * a script that prints My number: <first argument converted in integer>
 * if the first argument can be converted to an integer:
*/
const args = require('process').argv;
let response;
if (isNaN(Number(args[2]))) response = 'Not a number';
else response = 'My number: ' + args[2];
console.log(response);
