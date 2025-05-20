const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = 1245;
const DATABASE = path.join(__dirname, 'database.csv');

app.get('/', (req, res) => {
  res.status(200).send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  try {
    const data = fs.readFileSync(DATABASE, 'utf8').trim();
    const lines = data.split('\n').filter(line => line.trim() !== '');
    const students = lines.slice(1);

    const fields = {};
    for (const line of students) {
      const [firstName, , , field] = line.split(',');
      if (!fields[field]) fields[field] = [];
      fields[field].push(firstName);
    }

    let response = 'This is the list of our students\n';
    response += `Number of students: ${students.length}\n`;

    for (const field in fields) {
      response += `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}\n`;
    }

    res.status(200).send(response.trim());
  } catch (error) {
    res.status(500).send('Cannot load the database');
  }
});

app.listen(PORT, () => {
});
