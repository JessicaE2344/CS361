import zmq

def get_socket():
    """Create and return a ZeroMQ socket configured to connect to the microservice."""
    context = zmq.Context()
    socket = context.socket(zmq.REQ)  # REQ socket for sending requests
    socket.connect("tcp://localhost:5555")
    return socket

# Function to store game data
def store_game_data(socket, initials, difficulty, time_taken):
    """Send game data to be stored via the microservice."""
    try:
        socket.send_json({'action': 'store', 'initials': initials, 'difficulty': difficulty, 'time_taken': time_taken})
        response = socket.recv_json()
        print("Store Response:", response)
    except zmq.ZMQError as e:
        print(f"Failed to send/receive data: {e}")

# Function to retrieve game data
def retrieve_game_data(socket, initials):
    """Retrieve game data from the microservice."""
    try:
        socket.send_json({'action': 'retrieve', 'initials': initials})
        response = socket.recv_json()
        print("Retrieve Response:", response)
    except zmq.ZMQError as e:
        print(f"Failed to send/receive data: {e}")


def retrieve_all_data(socket):
    """Retrieve all game data from the microservice."""
    try:
        socket.send_json({'action': 'retrieve_all'})
        response = socket.recv_json()
        return response
    except zmq.ZMQError as e:
        print(f"Failed to send/receive data: {e}")




