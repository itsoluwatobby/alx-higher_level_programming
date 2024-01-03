#!/usr/bin/node
/**
 * a script that prints all characters of a Star Wars movie:
*/

const request = require('request');

const id = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${id}`, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const result = JSON.parse(body);
    const characters = result.characters;
    makeRequests(characters);
  } else {
    console.log(error);
  }
});

function makeRequests (urls) {
  if (!urls.length) return;
  const url = urls.shift();
  request(url, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const actor = JSON.parse(body);
      console.log(actor.name);
      return makeRequests(urls);
    } else {
      console.log(error);
    }
  });
}
