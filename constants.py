# the indices of the winning positions.
WINNERS = set()
WINNERS.add((0,1,2))
WINNERS.add((3,4,5))
WINNERS.add((6,7,8))
WINNERS.add((0,3,6))
WINNERS.add((1,4,7))
WINNERS.add((2,5,8))
WINNERS.add((0,4,8))
WINNERS.add((2,4,6))

# "a discount factor... used to balance immediate and future reward."
GAMMA = 0.9

# number of training epochs
EPOCHS = 100000

# the percent you want to explore while training
EPSILON = 0.3

# for replaying the game
AFFIRMATIVE = ['y', 'yes', 'yeah', "yea", 'ye']
