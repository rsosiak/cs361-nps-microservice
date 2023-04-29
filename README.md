# CS361 National Park Service Microservice

The microservice uses ZeroMQ to transfer data between the server and client.

## Setup

### Receiving an API key
To have the ability to send requests and receive data from the National Park Service API, an API key is needed. One can receive an API key by filling out the form on the National Park Service website (https://www.nps.gov/subjects/developer/get-started.htm).

### Running the server
Download `server.py` in the same directory as the client. Start the server by running `py server.py`.

### Running the client
Download `client.py` in the same directory as the client. The client will send example requests when you run `py client.py`.

## How to REQUEST data from the microservice
Requests are sent via string messages. Requests should be a string consisting of a two character state abbreviation (e.g., New York's two character state abbreviation is NY). 

A full list of state abbreviations can be found here: https://www.bls.gov/respondents/mwr/electronic-data-interchange/appendix-d-usps-state-abbreviations-and-fips-codes.htm.

Currently, there is one endpoint in the microservice. A user can send a request (a two character state abbreviation). If valid, a response will be sent back.

## How to RECEIVE data from the microservice

When a request is made to the server, the server will perform a GET request. In this case, the {message} is the request sent by the client, and the NPS_API_KEY is your specific API key.
`
  response = requests.get(f'https://developer.nps.gov/api/v1/'parks?stateCode={message}&api_key={NPS_API_KEY}'
`

When a request is successful, the response is parsed as a JSON object and sent back to the client via the socket.

Note: It's recommended that you do not hardcode your API key directly into your code. Instead, you can use a .env file in the root of your project folder that contains your API key. You can load your environment variables using the dotenv Python library, and more specifically, the load_dotenv method. More info on this package can be found here: https://pypi.org/project/python-dotenv/.

## UML sequence diagram

![image](https://user-images.githubusercontent.com/47833214/235327739-038d99b2-1c9a-41a8-a769-c66f56874b6e.png)

Request message is a string consisting of a two character state abbreviation (e.g., NY, TX, UT).

Returns a response containing National Park Service data for that state (see example response for 'TX': https://github.com/rsosiak/cs361-nps-microservice/blob/main/example_response.json).
