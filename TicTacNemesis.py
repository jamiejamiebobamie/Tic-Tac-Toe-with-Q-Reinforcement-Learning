import random

def check_winner(state):
    WINNERS = set()
    WINNERS.add((0,1,2))
    WINNERS.add((3,4,5))
    WINNERS.add((6,7,8))
    WINNERS.add((0,3,6))
    WINNERS.add((1,4,7))
    WINNERS.add((2,5,8))
    WINNERS.add((0,4,8))
    WINNERS.add((2,4,6))

    X = set()
    O = set()

    for i, board_space in enumerate(state):
        if board_space == 1:
            X.add(i)
        elif board_space == 0:
            O.add(i)

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
        Like longterm memory.

        All actions are set to an intial value of zero.

    """

    states_dictionary = {}

    # log the intial empty board as a state.
    states_dictionary[(None,None,None,None,None,None,None,None,None)] = [0,0,0,
                                                                0,0,0, 0,0,0]
    count = 0
    # one hundred thousand is enough games to generate all states
    while count < 100000:

        board = [None,None,None,None,None,None,None,None,None]
        Xs_turn = bool(random.getrandbits(1))

        while None in board:

            move_here = pick_random_move(board)

            if Xs_turn:
                board[move_here] = 1
                Xs_turn = False
            else:
                board[move_here] = 0
                Xs_turn = True

            state = tuple(board)

            # log the state and actions
            if state not in states_dictionary:

                # all states of Q should be initialized to 0
                states_dictionary[state] = [0,0,0, 0,0,0, 0,0,0]

        count += 1

    print("Done initializing Q.")
    return states_dictionary # 8953 possible states

def compute_R(state):
    """
        Returns the reward array for the current state.
        "Short term" memory.

    """
    R = [] # possible actions given current state
    for board_position in state:
        if board_position == None:
            R.append(0)
        else:
            R.append(-1)

    # check to see if any of the current moves create a winning scenario
        # ...

    return R

def pick_random_move(state):
    """
        Determine which indices into the board array contain None.
        These are the possible moves.

        Returns the index into the state array of the next move.

    """

    possible_moves = []
    for i, moves in enumerate(state):
        if moves == None:
            possible_moves.append(i)

    random_index_into_possible_moves = random.randint(0,
                                                len(possible_moves)-1)

    return possible_moves[random_index_into_possible_moves]

def play_tictactoe_turn(state, turn):
    move_here = pick_random_move(state)
    board_state = list(state)

    if turn:
        board_state[move_here] = 1
        turn = False
    else:
        board_state[move_here] = 0
        turn = True

    new_board_state = tuple(board_state)

    # update appropriate Q model here
    # Q_models[!turn][state][move_here] = 50
    # print(state, !turn, Q_models[!turn][state],Q_models[!turn][state][move_here])

    return new_board_state, turn

Q_0 = generate_initial_Q()
Q_X = generate_initial_Q()

Q_models = { True: Q_X, False: Q_0 }

winner = None

for _ in range(1):
    board = [None,None,None,None,None,None,None,None,None]
    board_state = tuple(board)

    # X's turn equals True, O's turn equals False
    turn = bool(random.getrandbits(1))

    while winner == None:
        board_state, turn = play_tictactoe_turn(board_state, turn)
        # print(board_state)
        winner = check_winner(board_state)
    else:
        # print(winner)
        winner = None

# Q(state, action) = R(state, action) + Gamma * Max[Q(next state, all actions)]
# Q(1, 5) = R(1, 5) + 0.8 * Max[Q(5, 1), Q(5, 4), Q(5, 5)] = 100 + 0.8 * 0 = 100
