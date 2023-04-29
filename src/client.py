import json

import zmq

context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.connect('tcp://localhost:5555')

print('Sending request...')
socket.send_string('Getting JSON response...')

message = socket.recv()
message = json.loads(message)
print('Received reply...')
print(message['id'])
