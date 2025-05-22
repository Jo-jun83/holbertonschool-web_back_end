const app = require('http');

app.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.write('Hello Holberton School!');
  res.end();
});
app.listen(1245);

module.exports = app;
