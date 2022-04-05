#!/usr/bin/node
const args = process.argv;
const number1 = parseInt(args[2]);
const number2 = parseInt(args[3]);
function add (number1, number2) {
  return number1 + number2;
}
console.log(add(number1, number2));
