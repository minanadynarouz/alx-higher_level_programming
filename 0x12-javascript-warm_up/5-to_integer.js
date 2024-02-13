#!/usr/bin/node

let num = Number(process.argv[2]);

if (!isNaN(num)) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
