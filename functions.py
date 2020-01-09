from constants import *
import random

def check_winner(state):
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
    for i, board_space in enumerate(state):
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

    if len(X) + len(O) == len(state):
        return -1 # tie

def generate_initial_Q():
    """
        This builds the initial brain or 'Q'.
        Returns a dictionary of states associated with an array of actions.
        All actions are set to an intial value of zero.

    """

    states_dictionary = {}

    # log the intial empty board as a state.
    empty_board = (None,None,None,None,None,None,None,None,None)
    states_dictionary[empty_board] = [0,0,0,0,0,0,0,0,0]

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

def compute_R(state, turn):
    """
        Returns the reward array for the current state.
        "Short term" memory / immediate gratification.

    """
    # sets of indices where X has gone, O has gone, and no one has gone.
    X = set()
    O = set()
    N = set()
    R = [] # possible actions given current state
    for i, board_position in enumerate(state):
        if board_position == None:
            R.append(0)
            N.add(i)
        else:
            R.append(-1)
            if board_position == 1:
                X.add(i)
            else:
                O.add(i)

    possible_winners_X = X|N
    possible_winners_O = N|O

    for i, score in enumerate(R):
        if score != -1:
            if i in possible_winners_X:
                R[i] += 1
            if i in possible_winners_O:
                R[i] += 1

    return R

def pick_random_move(state):
    """
        Determine which indices into the board array contain None.
        These are the possible moves.

        Returns the index into the state array of the next move.

    """
    move_array = get_available_moves(state)
    length_of_move_array = len(move_array)

    random_index_into_possible_moves = random.randint(0,
                                                length_of_move_array-1)

    return move_array[random_index_into_possible_moves]


def get_available_moves(state):
    """
        Determine which indices into the board array contain None.
        These are the possible moves.

        Returns the index into the state array of the next move.

    """
    possible_moves = []
    for i, moves in enumerate(state):
        if moves == None:
            possible_moves.append(i)

    return possible_moves

def play_tictactoe_turn_training(Q, state, turn):
    """
        Play a single turn of tic tac toe while training. Updates the Q model.
        Returns the new board state and the next person's turn.
    """

    R = compute_R(state,turn)

    if random.uniform(0, 1) < epsilon:
        # exploration
        action = pick_random_move(state)
    else:
        # exploitation
        max_action = float("-inf")
        store_index_of_max_equals = []
        for i, action in enumerate(R):
            temp = max_action
            if action == max_action:
                store_index_of_max_equals.append(i)
            elif action > max_action:
                store_index_of_max_equals = []
                store_index_of_max_equals.append(i)
            max_action = max(max_action,action)
        action = random.choice(store_index_of_max_equals)

    board_state = list(state)
    if turn:
        board_state[action] = 1
        turn = False
    else:
        board_state[action] = 0
        turn = True
    new_board_state = tuple(board_state)

    """
    Q(state, action) =
        R(state, action) + Gamma * Max[Q(next state, all actions)]
    """
    Q[state][action] = R[action] + GAMMA * max(Q[new_board_state])

    return new_board_state, turn


def play_tictactoe_turn(action, state, turn):
    """
        Play a single turn of tic tac toe.
        Returns the new board state and the next person's turn.
    """

    board_state = list(state)
    if turn:
        board_state[action] = 1
        turn = False
    else:
        board_state[action] = 0
        turn = True
    new_board_state = tuple(board_state)

    return new_board_state, turn

def test_Q_with_state(Q, state):
    """
        Given a trained brain, Q, and a board state:
            (0, 1, 0, 1, None, None, None, None, 0)
        recieve an index in the board state for the suggested next move.
    """
    valid_state = Q.get(state, None)
    if valid_state == None:
        return "Not valid board state."

    winner = check_winner(state)
    if winner != None:
        return "There is already a winner."

    min_indices = set()
    min_choice = float("inf")
    for i, choice in enumerate(Q[state]):
        temp = min_choice
        if choice != 0:
            min_choice = min(min_choice,choice)
        if temp != min_choice:
            min_indices = set()
            min_indices.add(i)
        if choice == min_choice:
            min_indices.add(i)

    return random.choice(list(min_indices))

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
