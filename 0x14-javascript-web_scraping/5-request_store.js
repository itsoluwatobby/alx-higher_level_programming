#!/usr/bin/node
/**
 * a script that gets the contents of a webpage and stores it in a file.
 */

const request = require('request');
const fs = require('fs').promises;
const path = require('path');

const url = process.argv[2];
const filename = process.argv[3];

request(url, async (error, response, body) => {
  if (!error && response.statusCode === 200) {
    await fs.writeFile(path.join(__dirname, filename), body, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  } else {
    console.log(error);
  }
});
