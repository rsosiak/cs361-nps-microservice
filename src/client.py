import json

import zmq

context = zmq.Context()

print('Connecting to server...')
socket = context.socket(zmq.REQ)
socket.connect('tcp://localhost:5555')

requests = ['NY', 'TX', 'ME']
for request in requests:
    print(f'Sending request {request}')
    socket.send_string(request)

    message = socket.recv()
    message = json.loads(message)
    print('Received reply:')
    print(message)
