#!/usr/bin/node
const { dict } = require('./101-data');
function modifyList (dict) {
  const result = {};
  Object.entries(dict).map(([key,value]) => {
    if(result.hasOwnProperty(value)) result[value].push(key);
    else result[value] = [key];
  });
  console.log(result);
}
modifyList(dict);
