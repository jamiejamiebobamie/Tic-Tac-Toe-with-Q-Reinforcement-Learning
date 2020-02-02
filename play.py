from functions import play_game, convert_csv_to_Q

# load a.i.
file_path = 'pickled_brain3.csv'
Q = convert_csv_to_Q(file_path)

# play
print("Let's play!\n")
play_game(Q)
print("\nThanks for playing!")
