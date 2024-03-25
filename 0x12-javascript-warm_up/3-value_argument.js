#!/usr/bin/node
const process = require('process'); // Access arguments passed to the script

const Argpresent = process.argv.length > 2;

if (Argpresent)
{
        console.log("Argument found");
}
else
{
        console.log("No argument");
}
