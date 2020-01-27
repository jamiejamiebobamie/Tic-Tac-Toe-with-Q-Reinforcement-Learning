from constants import EPOCHS
from functions import (generate_initial_Q, train, test_accuracy,
                        test_single_moves, convert_csv_to_Q)

# initialize
# print("Initializing Q.")
# Q = generate_initial_Q()
# print("Done initializing Q.\n")
#
# # train
# print("Begin training.")
# train(EPOCHS, Q)
# print("Done training.\n")

file_path = 'pickled_brain2.csv'
Q = convert_csv_to_Q(file_path)

# test
print("Begin testing.")
test_accuracy(100, Q)
# test_single_moves(20, Q)
# print(Q)
print("Done testing.\n")
