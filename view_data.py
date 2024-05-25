# view_data.py
from game_client import get_socket, retrieve_game_data, retrieve_all_data

def view_data():
    socket = get_socket()
    initials = input("Enter initials to view specific results or leave blank to view all results: ").strip().upper()
    if initials:
        response = retrieve_game_data(socket, initials)
    else:
        response = retrieve_all_data(socket)

    if response and response.get('data'):
        print("Retrieved Data:", response['data'])
    else:
        print("")

    socket.close()

if __name__ == "__main__":
    view_data()
