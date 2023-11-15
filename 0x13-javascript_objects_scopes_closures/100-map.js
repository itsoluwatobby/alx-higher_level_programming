#!/usr/bin/node
const { list } = require('./100-data');
function modifyList (list) {
  const newList = list.map((num, index) => num * index);
  console.log(list);
  console.log(newList);
}
modifyList(list);
