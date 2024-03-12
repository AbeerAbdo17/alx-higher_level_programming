#!/usr/bin/node

exports.converter = function (base) {
  return function (xnum) {
    return xnum.toString(base);
  };
};
