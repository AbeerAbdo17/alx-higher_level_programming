#!/usr/bin/node
exports.esrever = function (list) {
  const xrev = [];
  for (let xv = list.length - 1; xv >= 0; xv--) {
    xrev.push(list[xv]);
  }
  return xrev;
};
