from constants import *
from functions import *

# initializing the brain
print("Initializing Q.")
Q = generate_initial_Q()
print("Done initializing Q.\n")

winner = None

# training
print("Begin training.")
for epoch in range(epochs):
    board = [None,None,None,None,None,None,None,None,None]
    board_state = tuple(board)

    # X's turn equals True, O's turn equals False
    turn = bool(random.getrandbits(1))

    while winner == None:
        board_state, turn = play_tictactoe_turn_training(Q, board_state, turn)
        winner = check_winner(board_state)
    else:
        winner = None
        percent = epoch/epochs
        if not percent % .01:
            print(percent *100, "% done.")

print("Done training.\n")
number_of_games = epochs
test_accuracy(number_of_games, Q)
