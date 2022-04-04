#!/usr/bin/node
const args = process.argv;
if (!args) {
  console.log('No argument');
} else {
  args.forEach(element => {
    if (args.indexOf(element) > 1) {
      console.log(element);
    }
  });
}
