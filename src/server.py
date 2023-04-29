import json
import os
import requests

import zmq

from dotenv import load_dotenv

load_dotenv()

NPS_API_KEY = os.getenv('NPS_API_KEY')

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind('tcp://*:5555')

while True:
    message = socket.recv()
    print(f'Received request: {message}')
    message = message.decode('UTF-8')

    response = requests.get(
        'https://developer.nps.gov/api/v1/' +
        f'parks?stateCode={message}&api_key={NPS_API_KEY}'
    )

    result = response.json()['data']

    print(f'Sending result for message: {message}')
    socket.send_string(json.dumps(result))
