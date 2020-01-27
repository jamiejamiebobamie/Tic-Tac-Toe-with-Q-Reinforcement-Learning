from constants import EPOCHS
from functions import (generate_initial_Q, train, test_accuracy,
                        test_single_moves)

# initialize
print("Initializing Q.")
Q = generate_initial_Q()
print("Done initializing Q.\n")

# train
print("Begin training.")
train(EPOCHS, Q)
print("Done training.\n")


# test
print("Begin testing.")
# test_accuracy(100000, Q)
test_single_moves(20, Q)
# print(Q)
print("Done testing.\n")
