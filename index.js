const fs = require('fs');
const dir = './Writeups';

fs.readdir(dir, (err, files) => {
  console.log(files.length);
});
