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
    Promise.all(characters.map(async (actorUrl) => {
      await request(actorUrl, (error, response, body) => {
        if (!error && response.statusCode === 200) {
          const actor = JSON.parse(body);
          console.log(actor.name);
        } else {
          console.log(error);
        }
      });
    }));
  } else {
    console.log(error);
  }
});
