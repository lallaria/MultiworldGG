// list-files.js

const fs = require('fs');
const path = require('path');

// Change this to the folder you want to list
const folderPath = __dirname;

fs.readdir(folderPath, (err, files) => {
  if (err) {
    console.error(`Error reading directory ${folderPath}:`, err);
    process.exit(1);
  }

  // Strip extensions and collect base names
  const baseNames = files.map(file => path.parse(file).name);

  // Output the list
  baseNames.forEach(name => console.log(name));
});
