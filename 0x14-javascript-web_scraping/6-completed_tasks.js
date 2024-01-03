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
    for (const todo of todos) {
      if (todo.completed) result[todo.userId] = todo.id;
    }
    console.log(result);
  } else {
    console.log(error);
  }
});
