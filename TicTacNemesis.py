import random

def generate_initial_Q():
    """
        This builds the initia; brain or 'Q',
        a dictionary of states associated with an array of actions.
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
        Creates the reward matrix for the current state.
        "Short term" memory.

    """
    R = [] # possible actions given current state
    for board_position in state:
        if board_position == None:
            R.append(0)
        else:
            R.append(-1)
    return R

def pick_random_move(state):
    """
        Determine which indices into the board array contain None.
        These are the possible moves.

    """

    possible_moves = []
    for i, moves in enumerate(state):
        if moves == None:
            possible_moves.append(i)

    random_index_into_possible_moves = random.randint(0,
                                                len(possible_moves)-1)

    return possible_moves[random_index_into_possible_moves]


Q = generate_initial_Q()

# Q(state, action) = R(state, action) + Gamma * Max[Q(next state, all actions)]
# Q(1, 5) = R(1, 5) + 0.8 * Max[Q(5, 1), Q(5, 4), Q(5, 5)] = 100 + 0.8 * 0 = 100
