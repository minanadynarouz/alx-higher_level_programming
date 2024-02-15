#!/usr/bin/node

const importedList = require('./100-data.js').list;
let newArr = importedList.map((num, idx) => num * idx);
console.log(importeList);
console.log(newArr);
