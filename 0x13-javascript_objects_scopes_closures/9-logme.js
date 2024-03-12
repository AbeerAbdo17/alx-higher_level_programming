#!/usr/bin/node
let xcoun = 0;

exports.logMe = function (item) {
  console.log(xcoun + ': ' + item);
  xcoun++;
};
