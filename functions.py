from constants import *
import random

# -- - general_purpose methods - - --- - -
def check_winner(board_state):
    """
        Time complexity : O(33)
        Iterates over the board spaces,
        Recording the indices of 1's (1) and 0's (0) in two sets.

        Iterates through the winning combinations in WINNERS
        to see if there is a winner.

        Returns 1, 0, or -1 if 1 wins, 0 wins,
        or if there is a tie, respectively.

        Returns None if there is no winner or tie.

        (1 and 0 can represent X's or O's in the game
        and either 1 or 0 can go first.)
    """

    indices_ones = set()
    indices_zeroes = set()

    # iterate over board spaces. record indices in sets.
    for i, board_position in enumerate(board_state):
        if board_position == 1:
            indices_ones.add(i)
        elif board_position == 0:
            indices_zeroes.add(i)

    # iterate through the set of winner tuples.
    # for each item in a winning configuration, check
    # if the item is contained in one of the sets.
    for winner in WINNERS:
        One_count = 0
        Zero_count = 0
        for w in winner:
            if w in indices_ones:
                One_count += 1
            elif w in indices_zeroes:
                Zero_count += 1

        # 1 wins
        if One_count == 3:
            return 1
        # 0 wins
        elif Zero_count == 3:
            return 0

    # tie
    if len(indices_ones) + len(indices_zeroes) == len(board_state):
        return -1

def generate_initial_Q():
    """
        This builds the initial brain or 'Q'.
        Returns a dictionary of states associated with an array of actions.
        All actions are set to an intial value of zero.
    """
    # 'Q' stands for 'Quality'.
    Q = {}
    # a dictionary of states:
    #       state = (turn, board_state)
    # associated with actions:
    #       actions = [0,0,0,0,0,0,0,0,0]
    # Q = { state: actions }


    # log the intial empty board and player's turn (True or False) as a state.
    state = (True, (None,None,None,None,None,None,None,None,None))
    # actions are all initialized to zero. action indices are associated with
        # the indices of board positions.
    Q[state] = [0,0,0,0,0,0,0,0,0]

    state = (False, (None,None,None,None,None,None,None,None,None))
    Q[state] = [0,0,0,0,0,0,0,0,0]

    # play enough games to generate all states.
    for _ in range(100000):

        board = [None,None,None,None,None,None,None,None,None]
        board_state = tuple(board)
        turn = bool(random.getrandbits(1))
        state = (turn, board_state)

        winner = None
        while winner == None:

            board_state = state[1]
            move_here = pick_random_move(board_state)
            action = move_here
            state = play_tictactoe_turn(action, state)

            if state not in Q:
                Q[state] = [0,0,0, 0,0,0, 0,0,0]

            board_state = state[1]
            winner = check_winner(board_state)

    return Q # 8953 valid states, but 3**9 or 19683 in all

def compute_R(state):
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
        an array of int.
        the largest int being the best move / biggest reward.
        Immediate gratification.
    """
    turn, board_state = state

    # possible actions given current state
    Reward_Array = []

    # look for empty board_positions
    for i, board_position in enumerate(board_state):
        if board_position == None:
            Reward_Array.append(0)
        else:
            Reward_Array.append(-1)

    # builds up the values in the rewards array by iterating through the board
    # and testing if either the opponent or the player is one move away from
    # winning
    for i, reward in enumerate(Reward_Array):
        if reward != -1:

            test_board_state = list()
            # deep copy needed.
            for j, board_position in enumerate(board_state):
                if j != i:
                    test_board_state.append(board_position)
                else:
                    test_board_state.append(int(turn))

            possible_winner = check_winner(test_board_state)
            # if the possible winner equals the person's who turn it is.
            if possible_winner == turn:
                Reward_Array[i] += 100 # LOG WINNING MOVE.

            test_board_state = list()
            # deep copy needed.
            for j, board_position in enumerate(board_state):
                if j != i:
                    test_board_state.append(board_position)
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

    if number_of_possible_moves < 1:
        return -1

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
    for i, board_position in enumerate(board_state):
        if board_position == None:
            possible_moves.append(i)

    return possible_moves

def play_tictactoe_turn(action, state):
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

    turn, board_state = state

    board = list(board_state)
    board[action] = int(turn) # change this to True/False instead of 1/0
    turn = not turn
    new_board_state = tuple(board)

    new_state = (turn, new_board_state)

    return new_state

def suggest_move(Q, state):
    """
        Given a trained brain, Q, and a state:
            (1, (0, 1, 0, 1, None, None, None, None, 0))
        recieve an index into the board state for the suggested next move.
    """
    board_state = state[1]
    winner = check_winner(board_state)
    # there is already a winner.
    if winner != None:
        return -1

    max_indices = set()
    max_choice = float("-inf")

    # test to see if the move is in the dictionary.
    valid = Q.get(state, None)

    # if it is not, add an empty set of actions to the brain.
    # this is a fail safe. this should never happen.
    if not valid:
        empty_actions = [0,0,0,0,0,0,0,0,0]
        new_entry = {state: empty_actions}
        Q.update(new_entry)
        print("NEW STATE ADDED! CHECK CODE. SOMETHING IS WRONG.")
        print(new_entry)

    Q_reward_array = Q[state]

    max_Q_action = int(max(Q_reward_array))
    # if the Q table is empty (all zeroes)
    # fallback on the Rewards Array
    if max_Q_action == 0:
        R = compute_R(state)
        index_of_max_R = get_index_of_max(R)
        return index_of_max_R

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
    state = (turn, board_state)

    winner = None
    player_symbol = None

    return board, state, winner, player_symbol

def get_index_of_max(iterable):
    max_i = -1
    max_v = float('-inf')

    for i, iter in enumerate(iterable):
        temp = max_v
        max_v = max(iter,max_v)
        if max_v != temp:
            max_i = i

    return max_i

# -- - end general_purpose methods - - --- - -

# training
def train(EPOCHS, Q):
    for epoch in range(EPOCHS):

        # ignore 'player_symbol' variable.
        board, state, winner, player_symbol = reset_game()

        while winner == None:
            last_state = state
            state = play_tictactoe_turn_training(Q, state)
            board_state = state[1]
            winner = check_winner(board_state)

        else:
            # reward winning state.
            winning_state = last_state
            reward_array = compute_R(winning_state)
            winning_actions = Q[winning_state]

            for i, reward in enumerate(reward_array):
                if reward >= 0:
                    winning_actions[i] += reward * LEARNING_RATE * GAMMA

            percent = epoch/EPOCHS
            if not percent % .01:
                print(percent *100, "% done.")

def play_tictactoe_turn_training(Q, state):
    """
        Play a single turn of tic tac toe while training.

        * * * UPDATES THE Q MODEL. * * *

        Returns the new board state and the next person's turn.
    """

    # the immediate rewards based on the given board_state
    R = compute_R(state)

    if random.uniform(0, 1) < EPSILON:
        # exploration
        board_state = state[1]
        action = pick_random_move(board_state)
    else:
        # exploitation
        action = suggest_move(Q, state)

    next_state = play_tictactoe_turn(action, state)

    # Update the Q model.
    Q[state][action] = ( (1 - LEARNING_RATE) * Q[state][action]
                                                + LEARNING_RATE
                                                * ( R[action] + GAMMA
                                                    * max(Q[next_state]) ) )

    return next_state

# testing / validation
def test_single_moves(num_moves, Q):
    for _ in range(num_moves):

        rand_state = random.choice(list(Q.keys()))
        turn, board_state = rand_state
        suggested_index_of_move = suggest_move(Q, rand_state)

        print("\nBoard State:")
        print(board_state[:3])
        print(board_state[3:6])
        print(board_state[6:9])
        print("Turn: ", int(turn))
        print("\nSuggested next move (0-8):")
        print(suggested_index_of_move)
        print(compute_R(rand_state))
        print(Q[rand_state])

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

            state = (turn, board_state)

            while winner == None:
                # play match.

                # use AI (or not)
                if AI == turn or AI == both:
                    suggested_move = suggest_move(Q, state)
                    action = suggested_move
                else:
                    board_state = state[1]
                    action = pick_random_move(board_state)

                state = play_tictactoe_turn(action, state)
                turn, board_state = state
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

    print("Testing when X goes first and O is using AI.")
    unit_test(first=X, AI=O, starting_percent=0)

    print("Testing when X goes first and both players have AI.")
    unit_test(first=X, AI=both, starting_percent=0)

    print("Testing when O goes first and O is using the AI.")
    unit_test(first=O, AI=O, starting_percent=0)

    print("Testing when O goes first and X is using AI.")
    unit_test(first=O, AI=X, starting_percent=0)

    print("Testing when O goes first and both players have AI.")
    unit_test(first=O, AI=both, starting_percent=0)

    print("Testing when X goes first and neither is using AI.")
    unit_test(first=X, AI=neither, starting_percent=0)

    print("Testing when O goes first and neither is using AI.")
    unit_test(first=O, AI=neither, starting_percent=0)


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

        board, state, winner, player_symbol = reset_game()
        player_symbol = pick_symbol()

        turn, board_state = state

        while winner == None:
            action = -1

            print("\nBoard State:")
            print_board_state(board_state, player_symbol)

            suggested_move = suggest_move(Q, state)

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

            state = play_tictactoe_turn(action, state)
            turn, board_state = state
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

# storing the model and unpacking the stored model for use.
import pandas as pd
import csv

def convert_Q_to_csv(Q, filepath):
    # https://stackoverflow.com/questions/8685809/writing-a-dictionary-to-a-csv-file-with-one-line-for-every-key-value
    pd.DataFrame.from_dict(data=Q, orient='index').to_csv(filepath, header=False)

# NEED TO CHANGE THIS METHOD FOR THE NEW KEY VALUE PAIR IN Q!
def convert_csv_to_Q(file_path):
    with open(file_path) as csv_file:
        reader = csv.reader(csv_file)
        # https://stackoverflow.com/questions/6740918/creating-a-dictionary-from-a-csv-file
        Q = dict()
        # currently keys are strings and values are not lists!
        for row in reader:

            turn = row[0][1]
            if turn == "T":
                turn = True
            else:
                turn = False

            key_list = row[0][2:-1].split(",")
            print(key_list) # this method is messed up.
            # for i, item in enumerate(key_list):
                # print(type(key_list[i]))
                # if item == ' 1':
                #     key_list[i] = 1
                # elif item == ' 0':
                #     key_list[i] = 0
                # elif item == 'N':
                #     print('hi')
                #     key_list[i] = None

            board_state = tuple(key_list)

            key = (turn, board_state)

            value = list()
            i = 1
            while i < len(row):
                new_value = float(row[i])
                value.append(new_value)
                i+=1
            Q.update( {key: value} )

    return Q
