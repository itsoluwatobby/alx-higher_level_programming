#!/usr/bin/node
/**
 * a script that display the status code of a GET request.
 */

const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (response.statusCode === 200) {
    console.log('code:', response.statusCode);
  } else {
    console.log(error);
  }
});
