#!/usr/bin/node
const process = require('process'); // Access arguments passed to the script

function Argcount(args)
{
	const numArgs = args.length - 2; // Exclude the first two arguments (script name and potentially Node.js path)

if (numArgs === 0)
{
	console.log("No argument");
}
else if (numArgs === 1)
{
	console.log("Argument found");
}
else
{
	console.log("Arguments found");
}
}

Argcount(process.argv); 
