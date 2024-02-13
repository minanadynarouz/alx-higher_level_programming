#!/usr/bin/node

function factorial (a) {
  if (a === 1) {
    return (1);
  } else {
    return (a * factorial(a - 1));
  }
}

const num1 = Number(process.argv[2]);

if (!isNaN(num1)) {
  console.log(factorial(num1));
} else {
  console.log(1);
}
