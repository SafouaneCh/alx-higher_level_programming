#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
	console.log('Missing number of occurrences');
} else { 
	let x = parseInt(process.argv[2]);
	while (x != 0) {
		console.log('C is fun');
		x = x - 1;
	}
}
