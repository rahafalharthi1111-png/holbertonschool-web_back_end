import fs from 'fs';

export default function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data
        .split('\n')
        .map((l) => l.trim())
        .filter((l) => l.length > 0);

      if (lines.length <= 1) {
        resolve({});
        return;
      }

      const header = lines[0];
      const rows = lines.slice(1);
      const cols = header.split(',').map((c) => c.trim());
      const idxFirst = cols.indexOf('firstname');
      const idxField = cols.indexOf('field');
      if (idxFirst === -1 || idxField === -1) {
        reject(new Error('Idx not in range'));
        return;
      }
      const groups = Object.create(null);
      for (const row of rows) {
        const cells = row.split(',').map((c) => c.trim());
        const firstname = cells[idxFirst];
        const field = cells[idxField];
        if (!groups[field]) {
          groups[field] = [];
        }
        groups[field].push(firstname);
      }

      resolve(groups);
    });
  });
}
