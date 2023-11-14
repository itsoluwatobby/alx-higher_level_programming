#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const num of list) searchElement === num && count++;
  return count;
};
