from constants import *
from functions import *

print("Initializing Q.")
Q = generate_initial_Q()
print("Done initializing Q.\n")

winner = None

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

player_symbol = None
while player_symbol != "X" and player_symbol != "O":
    print("Do you want to be X's or O's?")
    player_symbol = input()
    if player_symbol.isalpha():
        player_symbol = player_symbol.upper()

board = [None,None,None,None,None,None,None,None,None]
board_state = tuple(board)
turn = True

play_again = 'y'
while play_again in affirmative:
    while winner == None:
        suggested_move = test_Q_with_state(Q, board_state)
        action = -1
        if turn:
            possible_moves = get_available_moves(board_state)
            print("\nBoard State:")
            print_board_state(board_state, player_symbol)
            print("The possible moves (0-8) are:", possible_moves)
            print("From the available positions where would you like to go?")
            print("The algorithm thinks you should go here:", suggested_move)
            print()
            while action not in possible_moves:
                action = input()
                action = int(action)
        else:
            action = suggested_move

        board_state, turn = play_tictactoe_turn(action, board_state, turn)

        winner = check_winner(board_state)

    if winner == 1:
        print("You won!")
    elif winner == 0:
        print("You lost :(.")
    else:
        print("Tie!")

    print_board_state(board_state, player_symbol)

    # reset game
    board = [None,None,None,None,None,None,None,None,None]
    board_state = tuple(board)
    turn = True
    winner = None

    print("Would you like to play again?\n y / n ?\n")
    play_again = input()
    play_again = play_again.lower()
