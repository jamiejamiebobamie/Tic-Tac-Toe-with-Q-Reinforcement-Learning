from constants import *
import random

# -- - general_purpose methods - - --- - -
def check_winner(board_state):
    """
        Time complexity : O(33)
        Iterates over the board spaces,
        Recording the indices of X's (1) and O's (0) in two sets.

        Iterates through the winning combinations in WINNERS
        to see if there is a winner.

        Returns 1, 0, or -1 if X wins, O wins,
        or if there is a tie, respectively.

        Returns None if there is no winner or tie.
    """
    X = set()
    O = set()

    # O(9)
    for i, board_space in enumerate(board_state):
        if board_space == 1:
            X.add(i)
        elif board_space == 0:
            O.add(i)

    # O(8*3) = O(24)
    for winner in WINNERS:
        X_count = 0
        O_count = 0
        for w in winner:
            if w in X:
                X_count += 1
            elif w in O:
                O_count += 1
        if X_count == 3:
            return 1 # X wins
        elif O_count == 3:
            return 0 # O wins

    if len(X) + len(O) == len(board_state):
        return -1 # tie

def generate_initial_Q():
    """
        This builds the initial brain or 'Q'.
        Returns a dictionary of states associated with an array of actions.
        All actions are set to an intial value of zero.
    """
    states_dictionary = {}

    # log the intial empty board as a state.
    empty_board_state = (None,None,None,None,None,None,None,None,None)
    states_dictionary[empty_board_state] = [0,0,0,0,0,0,0,0,0]

    # one hundred thousand is enough games to generate all states
    for _ in range(100000):
        winner = None
        board = [None,None,None,None,None,None,None,None,None]
        turn = bool(random.getrandbits(1))

        while winner == None:

            move_here = pick_random_move(board)
            if turn: # X's turn
                board[move_here] = 1
                turn = False
            else: # O's turn
                board[move_here] = 0
                turn = True

            board_state = tuple(board)
            # log the state and actions
            if board_state not in states_dictionary:
                # all states of Q should be initialized to 0
                states_dictionary[board_state] = [0,0,0, 0,0,0, 0,0,0]

            winner = check_winner(board_state)

    return states_dictionary # 8953 possible states

def compute_R(board_state, turn):
    """
    Input:
         board_state:
            (0,1,0,None,None,None,None,None,None)
         a tuple of the board's state

         turn:
            1/0
         indicates if it's the first-person's turn (1) or the second's (0)
         (whoever originally went first)

    Output:
        an array of integers.
        the largest int being the best move / biggest reward.
        Immediate gratification.
    """

    # sets of indices where X has gone, O has gone, and no one has gone.
    X_position = set()
    O_position = set()
    None_position = set()
    Reward_Array = [] # possible actions given current state
    for i, board_position in enumerate(board_state):
        if board_position == None:
            Reward_Array.append(0)
            None_position.add(i)
        else:
            Reward_Array.append(-1)
            if board_position == 1:
                X_position.add(i)
            else:
                O_position.add(i)

    # builds up the values in the rewards array by iterating through the board
    # and testing if either the opponent or the player is one move away from
    # winning
    for i, reward in enumerate(Reward_Array):
        if reward != -1:

            test_board_state = list()
            # deep copy needed.
            for j, move in enumerate(board_state):
                if j != i:
                    test_board_state.append(move)
                else:
                    test_board_state.append(int(turn))

            possible_winner = check_winner(test_board_state)
            # if the possible winner equals the person's who turn it is.
            if possible_winner == turn:
                Reward_Array[i] += 100 # LOG WINNING MOVE.

            test_board_state = list()
            # deep copy needed.
            for j, move in enumerate(board_state):
                if j != i:
                    test_board_state.append(move)
                else:
                    test_board_state.append(int(not turn))

            possible_winner = check_winner(test_board_state)
            # if the possible winner equals the other guy.
            if possible_winner == (not turn):
                Reward_Array[i] += 50 # BLOCK THE OTHER PLAYER.

    return Reward_Array

def pick_random_move(board_state):
    """
    Input:
         board_state:
            (0,1,0,None,None,None,None,None,None)
         a tuple of the board's state

    Output:
         a random move from the possibilities.
    """
    possible_moves = get_available_moves(board_state)
    number_of_possible_moves = len(possible_moves)

    random_index_into_possible_moves = random.randint(0,
                                                number_of_possible_moves-1)

    return possible_moves[random_index_into_possible_moves]

def get_available_moves(board_state):
    """
    Input:
         board_state:
            (0,1,0,None,None,None,None,None,None)
         a tuple of the board's state

    Output:
         an array of board positions/indices of possible moves:
            [3,4,5,6,7,8]
    """
    possible_moves = []
    for i, moves in enumerate(board_state):
        if moves == None:
            possible_moves.append(i)

    return possible_moves

def play_tictactoe_turn(action, board_state, turn):
    """
    Input:
         action:
            0-8
         an index into the board array

         board_state:
            (0,1,0,None,None,None,None,None,None)
         a tuple of the board's state

         turn:
            1/0
         the player's who's turn it is

    Output:
         a new board state and the next person's turn:
            (0,1,0,None,None,None,None,None,1)
    """
    board = list(board_state)
    board[action] = int(turn)
    turn = not turn
    new_board_state = tuple(board)

    return new_board_state, turn

def suggest_move(Q, board_state):
    """
        Given a trained brain, Q, and a board state:
            (0, 1, 0, 1, None, None, None, None, 0)
        recieve an index into the board state for the suggested next move.
    """
    winner = check_winner(board_state)
    if winner != None:
        return -1 # there is already a winner.

    max_indices = set()
    max_choice = float("-inf")

    Q_reward_array = Q[board_state]

    # find all of the max positions from the Q for a given state.
    for i, choice in enumerate(Q_reward_array):
        if board_state[i] == None:
            temp = max_choice
            max_choice = max(max_choice, choice)
            if temp != max_choice:
                max_indices = set()
                max_indices.add(i)
            if choice == max_choice:
                max_indices.add(i)

    return random.choice(list(max_indices))

def reset_game():
    """
    'zero's' everything out.
    """
    board = [None,None,None,None,None,None,None,None,None]
    board_state = tuple(board)
    turn = bool(random.getrandbits(1))
    winner = None
    player_symbol = None
    return board, board_state, turn, winner, player_symbol
# -- - end general_purpose methods - - --- - -

# training
def train(EPOCHS, Q):
    for epoch in range(EPOCHS):

        # ignore 'player_symbol' variable.
        board, board_state, turn, winner, player_symbol = reset_game()

        while winner == None:
            board_state, turn = play_tictactoe_turn_training(Q,
                                                    board_state, turn)
            winner = check_winner(board_state)
        else:
            percent = epoch/EPOCHS
            if not percent % .01:
                print(percent *100, "% done.")

def play_tictactoe_turn_training(Q, board_state, turn):
    """
        Play a single turn of tic tac toe while training.

        * * * UPDATES THE Q MODEL. * * *

        Returns the new board state and the next person's turn.
    """

    R = compute_R(board_state, turn)

    if random.uniform(0, 1) < EPSILON:
        # exploration
        action = pick_random_move(board_state)
    else:
        # exploitation
        action = suggest_move(Q, board_state)

    board = list(board_state)
    board[action] = int(turn)
    turn = not turn
    new_board_state = tuple(board)

    # Update the Q model.
    Q[board_state][action] = ( (1 - LEARNING_RATE)
                                    * Q[board_state][action]
                                    + LEARNING_RATE * ( R[action]
                                    + GAMMA * max(Q[new_board_state])) )

    return new_board_state, turn

# testing / validation
def test_single_moves(num_moves, Q):
    for _ in range(num_moves):

        rand_state = random.choice(list(Q.keys()))
        suggested_index_of_move = suggest_move(Q, rand_state)

        print("\nBoard State:")
        print(rand_state[:3])
        print(rand_state[3:6])
        print(rand_state[6:9])

        print("\nSuggested next move (0-8):")
        print(suggested_index_of_move)

def test_accuracy(number_of_games, Q):
    def unit_test(first, AI, starting_percent=0):
        """
        Tests the Q model with the given parameters for the number_of_games
        Record it in the record dictionary.

        INPUT: 1/0, 1/0/-1, 0-100

        1/0 : who goes first x or o.
        1/0/-1/2 : who has ai, 1 for x, 0 for o, -1 for both, 2 for neither.
        starting_percent: increment the progress percent on the output display.
        """
        for game in range(number_of_games):
            board = [None,None,None,None,None,None,None,None,None]
            board_state = tuple(board)

            turn = first
            winner = None

            while winner == None:
                # play match.

                # use AI (or not)
                if AI == turn or AI == both:
                    suggested_move = suggest_move(Q, board_state)
                    action = suggested_move
                else:
                    action = pick_random_move(board_state)

                board_state, turn = play_tictactoe_turn(action,
                                                            board_state, turn)
                winner = check_winner(board_state)
            else:
                # record outcome.
                record[first][AI][winner] += 1

                # show progress.
                fraction = game/number_of_games
                if not fraction % .01:
                    print(fraction * 50+starting_percent, "% done.")

    # records a histogram of the outcomes of the games
    record = dict()

    # who won and how many times.
    X, O, tie = True, False, -1
    win_count1 = { X: 0, O: 0, tie: 0 }
    win_count2 = { X: 0, O: 0, tie: 0 }
    win_count3 = { X: 0, O: 0, tie: 0 }
    win_count4 = { X: 0, O: 0, tie: 0 }

    win_count5 = { X: 0, O: 0, tie: 0 }
    win_count6 = { X: 0, O: 0, tie: 0 }
    win_count7 = { X: 0, O: 0, tie: 0 }
    win_count8 = { X: 0, O: 0, tie: 0 }

    # who was using ai
    both, neither = -1, 2
    ai1 = { X: win_count1, O: win_count2, both: win_count3, neither: win_count4}
    ai2 = { X: win_count5, O: win_count6, both: win_count7, neither: win_count8}

    # who went first
    record[X] = ai1
    record[O] = ai2

    print("Testing when X goes first and X is using the AI.")
    unit_test(first=X, AI=X, starting_percent=0)

    print("Testing when O goes first and O is using the AI.")
    unit_test(first=O, AI=O, starting_percent=50)

    print("Testing when X goes first and both players have AI.")
    unit_test(first=X, AI=both, starting_percent=0)

    print("Testing when O goes first and both players have AI.")
    unit_test(first=O, AI=both, starting_percent=50)

    print("Testing when X goes first and neither is using AI.")
    unit_test(first=X, AI=neither, starting_percent=0)

    print("Testing when O goes first and neither is using AI.")
    unit_test(first=O, AI=neither, starting_percent=50)

    print("Testing when X goes first and O is using AI.")
    unit_test(first=X, AI=O, starting_percent=0)

    print("Testing when O goes first and X is using AI.")
    unit_test(first=O, AI=X, starting_percent=50)

    print(record)

# playing
def play_game(Q):
    def pick_symbol():
        player_symbol = None
        while player_symbol != "X" and player_symbol != "O":
            print("Do you want to be X's or O's?")
            player_symbol = input()
            if player_symbol.isalpha():
                player_symbol = player_symbol.upper()

        return player_symbol

    play_again = 'y'
    while play_again in AFFIRMATIVE:

        board, board_state, turn, winner, player_symbol = reset_game()
        player_symbol = pick_symbol()

        while winner == None:
            action = -1

            print("\nBoard State:")
            print_board_state(board_state, player_symbol)

            suggested_move = suggest_move(Q, board_state)

            if turn:
                possible_moves = get_available_moves(board_state)
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

        print("Would you like to play again?\n y / n ?\n")
        play_again = input()
        play_again = play_again.lower()

def print_board_state(board_state, player_symbol):
    if player_symbol == "X":
        computer_symbol = "O"
    else:
        computer_symbol = "X"

    board = []
    for i, position in enumerate(board_state):
        if position == 1:
            board.append(player_symbol)
        elif position == 0:
            board.append(computer_symbol)
        else:
            board.append(i)

    print(board[:3])
    print(board[3:6])
    print(board[6:9])
