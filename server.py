from flask import Flask, request
from threading import Lock
import time

app = Flask(__name__)

# Dictionary to track client requests and timestamps
client_requests = {}
# Lock for thread-safe operations on the dictionary
lock = Lock()


@app.route('/')
def index():
    client_id = request.args.get('clientId')
    if not client_id:
        return "Missing client ID", 400

    with lock:
        current_time = time.time()
        requests_info = client_requests.get(client_id, {'count': 0, 'start_time': current_time})

        # Check if we are within the 5-second window
        if current_time - requests_info['start_time'] > 5:
            # Reset the count and start time
            requests_info = {'count': 1, 'start_time': current_time}
            print(f"- - - - - open new time frame for client {client_id} at {current_time}")
        else:
            requests_info['count'] += 1
            print(f"- - - - - currently are {requests_info['count']} requests in this time frame for client {client_id} |", "*"*requests_info['count'])


        # Update the client request info
        client_requests[client_id] = requests_info

        if requests_info['count'] > 5:
            print(f"- - - - - client {client_id} has reached it's Rate limit. {5-(current_time - requests_info['start_time'])} seconds until time frame will end")
            return "Rate limit exceeded", 503

    return "OK", 200


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
