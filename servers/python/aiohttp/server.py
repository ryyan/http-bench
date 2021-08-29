import uuid
import json
import datetime

from aiohttp import web

async def EchoHandler(req):
    # Log request
    print('{} {} {} {}'.format(
        datetime.datetime.now(), req.remote, req.method, req.rel_url))

    # Parse parameters
    words = req.match_info.get('words', '')
    num = req.query.get('num', 0)

    # Verify parameters
    if words.lower() != 'helloworld' or int(num) != 1234567890:
        return web.Response(status=400, content_type='application/json',
                            body=json.dumps({'error': 'Invalid parameters'}))

    # Return response
    return web.Response(status=200, content_type='application/json',
                        body=json.dumps({'message': str(uuid.uuid4())}))


app = web.Application()
app.router.add_get('/echo/{words}', EchoHandler)
web.run_app(app, host='0', port=8888)
