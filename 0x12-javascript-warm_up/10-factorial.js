#!/usr/bin/node
const args = process.argv;
const number = parseInt(args[2]);
function factorial (number) {
  if (number === 0) {
    return 1;
  }
  if (!number) {
    return 1;
  }
  return number * factorial(number - 1);
}
console.log(factorial(number));
