#!/usr/bin/node
// a script that prints two arguments passed to it, in the following format: “ is ”
const args = process.argv;
const response = args[2] + ' is ' + args[3];
console.log(response);
