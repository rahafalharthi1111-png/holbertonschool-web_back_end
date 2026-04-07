import readDatabase from '../utils';

export default class StudentsController {
  static getAllStudents(req, res) {
    res.set('Content-Type', 'text/plain');
    const dbPath = process.argv[2];
    readDatabase(dbPath)
      .then((groups) => {
        const fields = Object.keys(groups)
          .sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));
        let body = 'This is the list of our students\n';
        for (const field of fields) {
          const count = groups[field].length;
          const list = groups[field].join(', ');
          body += `Number of students in ${field}: ${count}. List: ${list}\n`;
        }
        body = body.trimEnd();
        res.status(200).send(body);
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(req, res) {
    res.set('Content-Type', 'text/plain');
    const { major } = req.params;
    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }
    const dbPath = process.argv[2];
    readDatabase(dbPath)
      .then((groups) => {
        const names = groups[major] || [];
        const body = `List: ${names.join(', ')}`;
        res.status(200).send(body);
      })

      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }
}
