#!/usr/bin/node
function printMessage (...args) {
  if (args.length === None) {
    console.log('No argument');
  } else if (args.length === 1) {
    console.log('Argument found');
  } else {
    console.log('Arguments found');
  }
}

printMessage();
