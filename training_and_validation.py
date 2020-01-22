from constants import EPOCHS
from functions import generate_initial_Q, train, test_accuracy, test_single_moves

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

# test
print("Begin testing.")
test_accuracy(EPOCHS, Q1, Q2)
# test_single_moves(20, Q1, Q2)
# print(Q)
print("Done testing.\n")
