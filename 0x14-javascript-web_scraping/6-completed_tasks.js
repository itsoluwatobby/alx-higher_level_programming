#!/usr/bin/node
/**
 * a script that computes the number of tasks completed by user id.
 */

const request = require('request');

const url = process.argv[2];

request(url, async (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const todos = JSON.parse(body);
    const result = {};
    for (const x in todos) {
      if (todos[x].completed) {
        result[todos[x].userId] = (result[todos[x].userId] + 1) || 1;
      }
    }
    console.log(result);
  } else {
    console.log(error);
  }
});
