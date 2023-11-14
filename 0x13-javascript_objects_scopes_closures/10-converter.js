#!/usr/bin/node
exports.converter = function (base) {
  return function (sub) {
    return sub.toString(base);
  };
};
