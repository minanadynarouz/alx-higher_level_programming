#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;

  for (let i = 0; i < list.length - 1; i++) {
    if (searchElement === list[i]) {
      counter++;
    }
  }
}
