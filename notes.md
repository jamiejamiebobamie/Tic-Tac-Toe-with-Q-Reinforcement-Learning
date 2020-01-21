# Results from training_and_validation.py
{
 ## True: 														// X went first.
		{
			True: {True: 96963, False: 245, -1: 2792},           // X has the AI.
			False: {True: 20536, False: 79051, -1: 413},         // O has the AI.
			-1: {True: 100000, False: 0, -1: 0},                 // both have the AI.
			2: {True: 58063, False: 29097, -1: 12840}            // Neither have the AI.
		},
##	False:                                                       // O went first.
		{
			True: {True: 77757, False: 21910, -1: 333},
			False: {True: 0, False: 98313, -1: 1687},
			-1: {True: 0, False: 100000, -1: 0},
			2: {True: 28922, False: 58311, -1: 12767}
		}
}
### Out of a 400,000 games:
The player who goes first has a 58% chance of winning.
The accuracy of the built model is 96% when the player goes first and a 77-79%
when going second.

# ways to improve the model:

## Include who's turn it is in the Q model.
{x x _
o _ o
_ _ _}
^ ambiguous (who's turn is it?)

## maybe create two Q models / brains.
## one for the first person and one for the second.
