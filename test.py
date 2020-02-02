from functions import test_accuracy, convert_csv_to_Q

# load a.i.
file_path = 'pickled_brain3.csv'
Q = convert_csv_to_Q(file_path)

# test
print("Begin testing.")
number_of_games_per_unit_test = 10000
test_accuracy(number_of_games_per_unit_test, Q)
print("Done testing.\n")
