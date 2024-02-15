#!/usr/bin/node

const importedDict = require('./101-data.js').dict;
const newDict = {};

for (const key in importedDict) {
  const occurrence = importedDict[key];
  if (newDict[importedDict[key]] !== undefined) {
    newDict[occurrence].push(key);
  } else {
    newDict[occurrence] = [key];
  }
}

console.log(newDict);
