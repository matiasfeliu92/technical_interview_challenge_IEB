const http = require('http');

const options = {
  hostname: 'localhost',
  port: 8000,
  path: '/products/a08',
  method: 'GET'
};

const req = http.request(options, (res) => {
  console.log(`statusCode: ${res.statusCode}`);

  res.on('data', (chunk) => {
    console.log(chunk.toString());
  });

  res.on('end', () => {
    console.log('Data received');
  });
});

req.on('error', (error) => {
  console.error(error);
});

req.end();