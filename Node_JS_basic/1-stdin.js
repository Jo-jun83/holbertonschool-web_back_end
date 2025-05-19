const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Welcome to Holberton School, what is your name?\n", (name) => {
    console.log(`your name is: ${name} !`);
    rl.close("This important software is now closing");
});