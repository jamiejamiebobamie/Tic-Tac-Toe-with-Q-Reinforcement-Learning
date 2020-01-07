import random

WINNERS = set()
WINNERS.add((0,1,2))
WINNERS.add((3,4,5))
WINNERS.add((6,7,8))
WINNERS.add((0,3,6))
WINNERS.add((1,4,7))
WINNERS.add((2,5,8))
WINNERS.add((0,4,8))
WINNERS.add((2,4,6))

GAMMA = 0.8

def check_winner(state):

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
    # one hundred thousand is enough games to generate all states?
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

def compute_R(state, turn):
    """
        Returns the reward array for the current state.
        "Short term" memory.

    """
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

    # print(X,O)
    X_count = 0
    O_count = 0
    for winner in WINNERS:
        for w in winner:
            if w in X:
                X_count += 1
            elif w in O:
                O_count += 1

    # print(turn, X_count)

    possible_winners = set()
    if X_count >= 2 and turn == True:
        possible_winners = X|N
    elif O_count >= 2 and turn == False:
        possible_winners = O|N

    # print(possible_winners)

    for i, score in enumerate(R):
        if score == 0:
            if i in possible_winners:
                R[i] = 100

    # everything becomes ___ in the end...
    # print(R)

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

    # update appropriate Q model here
    Q_models[turn][state][move_here] = compute_R(state, turn)[move_here] + GAMMA * max(Q_models[turn][state])

    # print(Q_models[turn][state][move_here])
    if turn:
        board_state[move_here] = 1
        turn = False
    else:
        board_state[move_here] = 0
        turn = True

    new_board_state = tuple(board_state)
    return new_board_state, turn

Q_O = generate_initial_Q()
Q_X = generate_initial_Q()

Q_models = { True: Q_X, False: Q_O }

winner = None

for _ in range(100000):
    board = [None,None,None,None,None,None,None,None,None]
    board_state = tuple(board)

    # X's turn equals True, O's turn equals False
    turn = bool(random.getrandbits(1))

    while winner == None:
        board_state, turn = play_tictactoe_turn(board_state, turn)
        winner = check_winner(board_state)
    else:
        # print(winner)
        winner = None

print(Q_models[True])
