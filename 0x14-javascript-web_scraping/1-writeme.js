#!/usr/bin/node
/**
 * a script that writes a string to a file.
 */

const fs = require('fs');
const path = require('path');

const filename = process.argv[2];
const content = process.argv[3];

fs.writeFile(path.join(__dirname, filename), content, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
