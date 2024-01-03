#!/usr/bin/node
/**
 * a script that prints the number of movies where the character
 * “Wedge Antilles” is present.
 * Requirements:
 *  The first argument is the URL to request (GET)
 *  The status code must be printed like this: code: <status code>
 *  You must use the module request
 */

const request = require('request');

request('https://swapi-api.alx-tools.com/api/films', (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const res = JSON.parse(body);
    let count = 0;
    for (const x in res.results) {
      for (const c of res.results[x].characters) {
        if (c.includes('18')) {
          count++;
          break;
        }
      }
    }
    console.log(count);
  } else {
    console.log(error);
  }
});
