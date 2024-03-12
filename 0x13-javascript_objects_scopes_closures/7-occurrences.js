#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let xcount = 0;
  for (let xv = 0; xv < list.length; xv++) {
    if (searchElement === list[xv]) {
      xcount++;
    }
  }
  return xcount;
};
