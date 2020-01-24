from constants import EPOCHS
from functions import (generate_initial_Q, train, test_accuracy,
                        test_single_moves, convert_Q_to_csv, convert_csv_to_Q)

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
test_accuracy(100, Q)
# test_single_moves(20, Q)
# print(Q)
print("Done testing.\n")

print('Pickling brain.')
convert_Q_to_csv(Q)
print("Pickled and ready for future consumption.")

print("Testing if pickled brain worked.")
file_path = 'pickled_brain.csv'
pickled_Q = convert_csv_to_Q(file_path)
# print(pickled_Q)
# test_accuracy(EPOCHS, pickled_Q)
print("You'll know if it worked...")
