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
    response = requests.get(
        'https://developer.nps.gov/api/v1/' +
        f'parks?stateCode=TX&api_key={NPS_API_KEY}'
    )

    result = response.json()['data'][0]  # for testing, only return first row
    print(result)

    socket.send_string(json.dumps(result))
