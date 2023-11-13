#!/usr/bin/node
/**
 * a script that searches the second biggest integer in the
 * list of arguments.
 */
const args = require('process').argv;
if (args.length === 2 || args.length === 3) console.log(0);
else {
  const arg = args.slice(2);
  for (let i = 0; i < arg.length; i++) {
    for (let j = 0; j < arg.length; j++) {
      if (Number(arg[j]) < Number(arg[j + 1])) {
        const temp = Number(arg[j]);
        arg[j] = Number(arg[j + 1]);
        arg[j + 1] = temp;
      }
    }
  }
  console.log(arg[1]);
}
