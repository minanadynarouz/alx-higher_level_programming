#!/usr/bin/node

const num1 = Number(process.argv[2]);
const num2 = Number(process.argv[3]);

function add (a, b) {
  if (!isNaN(a) && !isNaN(b)) {
    console.log(a + b);
  } else if (isNaN(a) || isNaN(b)) {
    console.log(NaN);
  }
}

add(num1, num2);
