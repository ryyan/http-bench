import uuid
import json
import datetime

from flask import Flask, request, Response
app = Flask(__name__)

@app.route('/api/echo/<words>')
def EchoHandler(words):
    # Log request
    # Flask does it automatically

    # Parse path and query string parameters
    num = request.args.get('num', 0)

    # Verify parameters
    if words.lower() != 'helloworld' or int(num) != 1234567890:
        return Response(response=json.dumps({'error': 'Invalid parameters'}), status=400, mimetype='application/json')

	# Return response
    return Response(response=json.dumps({'message': str(uuid.uuid4())}), status=200, mimetype='application/json')


app.run(host='0.0.0.0', port=8888)
