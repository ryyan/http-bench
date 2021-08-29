const server = require('server');
const uuid = require('uuid');

const get = server.router.get;
const reply = server.reply;

async function EchoHandler(ctx) {
  // Log request
  console.log(`${new Date().toLocaleString()} ${ctx.ip} ${ctx.method} ${ctx.url}`);

  // Parse parameters
  let words = ctx.params.words
  let number = ctx.query.num

  // Verify parameters
  if (words.toLowerCase() !== 'helloworld' || parseInt(number) !== 1234567890) {
    return reply.status(400).json({error: 'Invalid parameters'});
  }

  // Return response
  return reply.status(200).json({message: uuid.v4()});
}

server({ port: 8888 }, [
  get('/echo/:words', async ctx => EchoHandler(ctx))
]);
