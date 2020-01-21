from constants import EPOCHS
from functions import generate_initial_Q, train, play_game

# initialize
print("Initializing Q.")
# the brain of the person that goes first
Q1 = generate_initial_Q()
# the brain of the person that goes second
Q2 = generate_initial_Q()
print("Done initializing Q.\n")

# train
print("Begin training.")
train(EPOCHS, Q1, Q2)
print("Done training.\n")

# play
print("Let's play!\n")
play_game(Q1,Q2)
print("\nThanks for playing!")
