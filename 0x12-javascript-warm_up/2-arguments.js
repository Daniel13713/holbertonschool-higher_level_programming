#!/usr/bin/node
switch (process.argv.length) {
  case 2:
    console.log('No argument');
    break;
  case 3:
    console.log('Argument found');
    break;
  case 4:
    console.log('Arguments found');
    break;
}
