#!/usr/bin/node
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];
const fs = require('fs');
const txtA = fs.readFileSync(fileA, 'utf8');
const txtB = fs.readFileSync(fileB, 'utf8');
fs.writeFileSync(fileC, txtA + txtB);
