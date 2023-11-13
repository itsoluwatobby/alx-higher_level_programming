#!/usr/bin/node
// a script that prints the first argument passed to it:
const args = process.argv;
let response;
if (args.length === 2) response = 'No argument';
else if (args.length > 2) response = args[2];
console.log(response);
