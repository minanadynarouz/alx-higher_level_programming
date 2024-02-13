#!/usr/bin/node

const len = process.argv.length;
const arr = process.argv.slice(2).map(Number);

if (len <= 2 || len === 3) {
  console.log(0);
} else {
  arr.sort((a, b) => b - a);
  console.log(arr[1]);
}
