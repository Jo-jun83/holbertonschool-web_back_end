const http = require('http');
const fs = require('fs');
const path = require('path');

const DATABASE = path.join(__dirname, 'database.csv');

const app = http.createServer((req, res) => {
  if (req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
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

      res.writeHead(200, { 'Content-Type': 'text/plain' });
      res.end(response.trim());
    } catch (error) {
      res.writeHead(500, { 'Content-Type': 'text/plain' });
      res.end('Cannot load the database');
    }
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('Not Found');
  }
});

app.listen(1245);
