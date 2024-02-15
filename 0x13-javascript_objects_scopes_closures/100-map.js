#!/usr/bin/node

const imported_list = require('./100-data.js').list;
let new_arr = imported_list.map((num, idx) => num * idx);
