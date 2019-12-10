const http = require('http');
const fs = require('fs');
const mime = require('mime');

const sendFile = function(res, filepath, data) {
  res.writeHead(200, {'content-type': mime.getType(filepath)});
  res.end(data);
};


const server = http.createServer((req, res) => {
  let filepath;
  if (req.url = '/') {
    filepath = './index.html';
  } else {
    filepath = './' + req.url;
  }

  fs.readFile(filepath, (err, data) => {
    if (err) {
      console.log('error');
    } else {
      sendFile(res, filepath, data);
    }
  });
});

server.listen(3000, () => {
  console.log('Running on port 3000');
});