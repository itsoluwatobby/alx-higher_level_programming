#!/usr/bin/node
/**
 * a script that prints the title of a Star Wars movie where the
 * episode number matches a given integer.
 * Requirements:
 *  The first argument is the URL to request (GET)
 *  The status code must be printed like this: code: <status code>
 *  You must use the module request
 */

const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const res = JSON.parse(body);
    console.log(res.title);
  } else {
    console.log(error);
  }
});
