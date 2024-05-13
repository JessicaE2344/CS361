# Microservice A to store data from Sudoku game

# Prerequisites- ZeroMQ

# To start server, run Python3 main.py

# To store game data I have included an example call and an example of what to include in your code once the game ends,
  def end_game(game):
    print("You've completed the Sudoku puzzle!")
    time_taken = int(input("Enter the total time taken to solve the puzzle (in seconds): "))
    difficulty = input("Enter the difficulty level (Easy, Medium, Hard): ").capitalize()
    while difficulty not in ["Easy", "Medium", "Hard"]:
        print("Invalid difficulty. Please choose Easy, Medium, or Hard.")
        difficulty = input("Enter the difficulty level (Easy, Medium, Hard): ").capitalize()
    initials = input("Enter your initials: ")

    socket = get_socket()
    store_game_data(socket, initials, difficulty, time_taken)
    print("Your game data has been saved. Congratulations!")

  # Example call: socket = get_socket()
  store_game_data(socket, 'XYZ', 'Medium', 570)

# How to retrieve data
Run view_data.py in the terminal.
Enter initials for game you want to view

The server in main.py will show data in a JSON format.

    
