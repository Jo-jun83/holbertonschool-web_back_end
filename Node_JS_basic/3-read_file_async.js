const fs = require('fs').promises;

async function countStudents(path) {
    try {
        const data = await fs.readFile(path, 'utf8');

        const lines = data.trim().split('\n');

        const students = lines.slice(1);

        console.log(`Number of students: ${students.length}`);

        const fields = {};
        for (const line of students) {
            const [firstName, lastName, age, field] = line.split(',');
            if (!fields[field]) {
                fields[field] = [];
            }
            fields[field].push(firstName);
        }

        for (const field in fields) {
            const names = fields[field].join(', ');
            console.log(`Number of students in ${field}: ${fields[field].length}. List: ${names}`);
        }
    } catch (error) {
        console.error('Erreur d\'origine :', error.message);
        throw new Error('Cannot load the database');
    }
}

module.exports = countStudents;
