#!/usr/bin/node
const args = process.argv;
const number = parseInt(args[2]);
if (number) {
  for (let i = 0; i < number; i++) {
    console.log('X'.repeat(number));
  }
} else {
  console.log('Missing size');
}
