#!/usr/bin/node


let length = process.argv.length;
let args = process.argv;

if (length < 3) {
	console.log("No argument");
} else if (length === 3) {
	console.log("Argument found");
} else {
	console.log("Arguments found");
}
