#!/usr/bin/node
// a script that prints a message depending of the number of arguments passed:
const args = process.argv;
let response;
if (args.length === 2) response = 'No argument';
else if (args.length === 3) response = 'Argument found';
else response = 'Arguments found';
console.log(response);
