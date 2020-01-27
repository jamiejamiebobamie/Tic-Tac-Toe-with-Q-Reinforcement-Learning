from constants import EPOCHS
from functions import (generate_initial_Q, train, test_accuracy,
                        test_single_moves, convert_Q_to_csv)

# initialize
print("Initializing Q.")
Q = generate_initial_Q()
print("Done initializing Q.\n")

# train
print("Begin training.")
train(EPOCHS, Q)
print("Done training.\n")

# pickle
print('Pickling model.')
filepath = 'pickled_brain2.csv'
convert_Q_to_csv(Q, filepath)
print("Done pickling.")
