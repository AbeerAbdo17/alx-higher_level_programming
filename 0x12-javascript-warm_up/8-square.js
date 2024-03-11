#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const xy = Number(process.argv[2]);
  let xv = 0;
  while (xv < xy) {
    console.log('X'.repeat(xy));
    xv++;
  }
}
