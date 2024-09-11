#!/usr/bin/node
function printArgum() {
	if (arguments[0] === undefined)
	{ console.log('No argument');
	} else {
		console.log(arguments[0]);
	}
}

printArgum();
printArgum("Hello");
