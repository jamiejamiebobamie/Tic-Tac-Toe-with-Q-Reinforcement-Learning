from constants import EPOCHS
from functions import generate_initial_Q, train, play_game

# initialize
print("Initializing Q.")
Q = generate_initial_Q()
print("Done initializing Q.\n")

# train
print("Begin training.")
train(EPOCHS, Q)
print("Done training.\n")

# play
print("Let's play!\n")
play_game(Q)
print("\nThanks for playing!")
