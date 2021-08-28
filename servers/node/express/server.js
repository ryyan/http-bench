const express = require('express')
const uuidv4 = require('uuid/v4');

function EchoHandler(req, res) {
  // Log request
  console.log(`${new Date().toLocaleString()} ${req.ip} ${req.method} ${req.originalUrl}`);

  // Parse parameters
  let words = req.params.words
  let number = req.query.num

  // Verify parameters
  if (words.toLowerCase() !== 'helloworld' || parseInt(number) !== 1234567890) {
    res.status(400).json({error: 'Invalid parameters'});
    return;
  }

  // Return response
  res.status(200).json({message: uuidv4()});
}

const app = express()
app.get('/api/echo/:words', (req, res) => EchoHandler(req, res));
app.listen(8888, () => console.log('Server listening on port 8888'));
