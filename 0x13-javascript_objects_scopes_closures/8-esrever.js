#!/usr/bin/node
exports.esrever = function (list) {
  const send = [];
  for (let j = list.length; j > 0; j--) {
    send.push(list[j - 1]);
  }
  return send;
};
