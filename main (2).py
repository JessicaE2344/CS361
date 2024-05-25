import zmq
import json  # for pretty printing of dictionaries for debugging

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

game_data = {}

while True:
    message = socket.recv_json()
    action = message['action']

    print("Current game data:", json.dumps(game_data, indent=4))  # Debugging output

    if action == 'store':
        initials = message['initials']
        difficulty = message['difficulty']
        time_taken = message['time_taken']
        if initials not in game_data:
            game_data[initials] = []
        game_data[initials].append((difficulty, time_taken))
        response = {'status': 'success'}
    elif action == 'retrieve':
        initials = message['initials']
        response = {'data': game_data.get(initials, [])}
    else:
        response = {'status': 'error', 'message': 'Invalid action'}

    socket.send_json(response)

