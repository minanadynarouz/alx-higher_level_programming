#!/usr/bin/node
exports.esrever = function (list) {
  return list.reduceRight((prev, current) => {
    prev.push(current);
    return prev;
  }, []);
};
