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

# testing / validation
for _ in range(30):
    rand_state = random.choice(list(Q.keys()))
    suggested_index_of_move = test_Q_with_state(Q, rand_state)
    print("\nBoard State:")
    print(rand_state[:3])
    print(rand_state[3:6])
    print(rand_state[6:9])
    print("\nSuggested next move (0-8):")
    print(suggested_index_of_move)
    print(Q[rand_state])
