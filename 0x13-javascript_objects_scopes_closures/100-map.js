#!/usr/bin/node

const importedList = require('./100-data.js').list;
const newArr = importedList.map((num, idx) => num * idx);
console.log(importedList);
console.log(newArr);
