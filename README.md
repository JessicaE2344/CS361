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

    
https://lucid.app/lucidchart/02c0fdcb-b9a3-44bd-ad59-866395548f14/edit?view_items=yYXBbz0VfpBv%2CbYXBEOZBRXUR%2CKZXBSrn1G65k%2CNTWBdttO7Cf.%2CNTWBKGTWqLqr%2CyZWBCiN-wVQA%2CNTWBFTp7lgg9%2CBZXBgtiTm7IE%2CRYWBIvROz9Zp%2CnYXB_nDKjiu8%2C30WBKzHy94U~%2C-0WBPw21ubKr%2CUYWB7SO4EKGq%2CaZWBCqUek~6z&invitationId=inv_6c0de13a-1cf3-4251-abb9-89811ba022c0

![B88E43CD-6353-48E0-8519-2EE0725BE005_1_201_a](https://github.com/JessicaE2344/CS361/assets/129296631/a5f0f19b-5b5e-4793-9373-00cbb2434259)
