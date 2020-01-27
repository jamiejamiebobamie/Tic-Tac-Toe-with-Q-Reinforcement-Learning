# Results from training_and_validation.py
{
 ## True: 														// X went first.
		{
			True: {True: 96038, False: 788, -1: 3174},           // X has the AI.
			False: {True: 4743, False: 83903, -1: 11354},         // O has the AI.
			-1: {True: 0, False: 0, -1: 100000},                 // both have the AI.
			2: {True: 58391, False: 28942, -1: 12667}            // Neither have the AI.
		},
##	False:                                                       // O went first.
		{
			True: {True: 79235, False: 6115, -1: 14650},
			False: {True: 548, False: 96858, -1: 2594},
			-1: {True: 0, False: 0, -1: 100000},
			2: {True: 28569, False: 58734, -1: 12697}
		}
}
### Out of 100,000 games:
The player who goes first has a 58% chance of winning.

The accuracy of the built model is 96-97% when the player goes first and 79-84%
when going second.

The games ended in a tie 100% of the time when both players were using the AI.

### Notes when brainstorming:

nine spots three possibilities per spot...
3^9 = 19683 total arrangements
only
8533
valid arrangements appear in dictionary.

[null, null, null,], [null, null, null,], [null, null, null,]

flattened 2d array
board = [null, null, null, null, null, null, null, null, null]

### Results when tuning hyperparameters and fixing algorithm:

{
True:
	{	True: 	{True: 44083, False: 42353, -1: 13564},
		False: 	{True: 0, False: 0, -1: 0},
		-1: {True: 67595, False: 11508, -1: 20897},
		2: {True: 58751, False: 28672, -1: 12577}
	},

False:
	{	True: {True: 0, False: 0, -1: 0},
		False: {True: 42389, False: 44083, -1: 13528},
		-1: {True: 11550, False: 67538, -1: 20912},
		2: {True: 0, False: 0, -1: 0}
	}
}


{
True:
	{	True: {True: 44006, False: 42453, -1: 13541},
		False: {True: 75020, False: 6886, -1: 18094},
		-1: {True: 66953, False: 11659, -1: 21388},
		2: {True: 58363, False: 28971, -1: 12666}
	},
False:
	{	True: {True: 0, False: 0, -1: 0},
		False: {True: 42661, False: 43881, -1: 13458},
		-1: {True: 11687, False: 67160, -1: 21153},
		2: {True: 0, False: 0, -1: 0}
	}
}


using test_Q_with_state_max in the unit test
// this is only good for the player who doesn’t have the ai, because the ai is never picking the right move.
{
True:
	{	True: {True: 43330, False: 42922, -1: 13748},
		False: {True: 75028, False: 6678, -1: 18294},
		-1: {True: 67142, False: 11259, -1: 21599},
		2: {True: 58506, False: 28856, -1: 12638}
	},
False:
	{	True: {True: 6530, False: 75178, -1: 18292},
		False: {True: 42984, False: 43357, -1: 13659},
		-1: {True: 12599, False: 66399, -1: 21002},
		2: {True: 28874, False: 58378, -1: 12748}
	}
}
epochs = 100 000
using test_Q_with_state (_min) in the unit test < — works! (at least better than picking randomly)
{
True: 																				// X went first.
	{	True: {True: 80384, False: 8723, -1: 10893}, 		// X has the AI - > ( 80384 / ( 80384 + 8723 + 10893 ) ) X won 80.384%
		False: {True: 39732, False: 52727, -1: 7541},		// O has the AI - > ( 52727 / ( 52727 + 39732 + 7541 ) ) O won 52.727%
		-1: {True: 71552, False: 20298, -1: 8150},				// both have the AI - > ( 71552 / ( 71552 + 20298 + 8150 ) ) X won 71.552%		
		2: {True: 58246, False: 28915, -1: 12839}				// neither has the AI - > ( 58246 / ( 58246 + 28915 + 12839 ) ) X won 58.246%
	},
False: 																				// O went first
	{	True: {True: 53031, False: 39481, -1: 7488}, 		// X has the AI - > ( 53031 / ( 53031 + 39481 + 7488 ) ) X won 53.031%
		False: {True: 8441, False: 79741, -1: 11818},		// O has the AI - > ( 79741 / ( 79741 + 8441 + 11818 ) ) O won 79.741%
		-1: {True: 19397, False: 72016, -1: 8587},				// both have the AI - > ( 72016 / ( 72016 + 19397 + 8587 ) ) O won 72.016%		
		2: {True: 29024, False: 58184, -1: 12792}				// neither has the AI - > ( 58184 / ( 58184 + 29024 + 12792 ) ) O won 58.184%
	}
}

// no real change.
epochs = 1 000 000
{
True:
	{	True: {True: 802006, False: 83970, -1: 114024},
		False: {True: 397982, False: 526938, -1: 75080},
		-1: {True: 721948, False: 194426, -1: 83626},
		2: {True: 584528, False: 288490, -1: 126982}
	},
False:
	{	True: {True: 526237, False: 398376, -1: 75387},
		False: {True: 84159, False: 801576, -1: 114265},
		-1: {True: 192167, False: 725091, -1: 82742},
		2: {True: 288334, False: 585359, -1: 126307}
	}
}

every time the trained ai was playing an ai that was picking at random and won.
(80,384 + 52,727 + 53,031 + 79,741) = 265, 883

every time the trained ai was playing an ai that was picking at random and lost.
(8723 + 39732 + 39481 + 8441) = 96,377

every time the trained ai was playing an ai that was picking at random and tied.
(10893 + 11818 + 7488 + 7541) = 37,740

66% accuracy
the AI wins 2/3rds of the games it plays, regardless of who goes first.







Messed everything up...
{
True:
	{	True: {True: 49354, False: 42933, -1: 7713},
		False: {True: 65311, False: 29615, -1: 5074},
		-1: {True: 53685, False: 44155, -1: 2160},
		2: {True: 58476, False: 28913, -1: 12611}
	},
False:
	{	True: {True: 23424, False: 69232, -1: 7344},
		False: {True: 44588, False: 48025, -1: 7387},
		-1: {True: 20321, False: 77920, -1: 1759},
		2: {True: 29083, False: 58276, -1: 12641}
	}
}
{
True:
	{	True: {True: 51116, False: 41031, -1: 7853},
		False: {True: 64116, False: 30764, -1: 5120},
		-1: {True: 55836, False: 42533, -1: 1631},
		2: {True: 58607, False: 28846, -1: 12547}
	},
False:
	{	True: {True: 24136, False: 68376, -1: 7488},
		False: {True: 42713, False: 49791, -1: 7496},
		-1: {True: 28506, False: 69424, -1: 2070},
		2: {True: 28989, False: 58348, -1: 12663}
	}
}



(0, None, None, None, None, 0, 1, None, None)

True None

[-1, 50, 1, 0, 0, -1, -1, 0, 0]

[-1, 50, 50, 0, 0, -1, -1, 0, 0]

[0, 0, 100.0, 90.0, 90.0, 0, 90.0, 0, 0]

(1, 1, None,
None, None, 0,
None, 0, 0)

[-1, -1, 100,
0, 0, -1,
0, -1, -1]

2


{
True:
	{
		True: {True: 83309, False: 7002, -1: 9689},
		False: {True: 33493, False: 65663, -1: 844},
		-1: {True: 80411, False: 18472, -1: 1117},
		2: {True: 58389, False: 28780, -1: 12831}
	},
False:
	{
		True:	 {	True: 65339, False: 33751, -1: 910},
		False: {True: 6233, False: 83888, -1: 9879},
		-1: {True: 12963, False: 86095, -1: 942},
		2: {True: 28856, False: 58567, -1: 12577}
	}
}

{
	True:
		{
			True: {True: 96963, False: 245, -1: 2792},
			False: {True: 20536, False: 79051, -1: 413},
			-1: {True: 100000, False: 0, -1: 0},
			2: {True: 58063, False: 29097, -1: 12840}
		},
	False:
		{
			True: {True: 77757, False: 21910, -1: 333},
			False: {True: 0, False: 98313, -1: 1687},
			-1: {True: 0, False: 100000, -1: 0},
			2: {True: 28922, False: 58311, -1: 12767}
		}
}

with two q’s one for first and one for second:
{
True:
	{
		True: {True: 80.9976, False: 15.4112, -1: 3.5912},
		False: {True: 16.9786, False: 81.6293, -1: 1.3921},
		-1: {True: 55.5867, False: 44.2942, -1: .1191},
		2: {True: 58.4489, False: 28.8155, -1: 12.7356}
	},
False:
	{
		True: {True: 42.0957, False: 44.9243, -1: 12.9800},
		False: {True: 14.7311, False: 65.9308, -1: 19.3381},
		-1: {True: 39.5640, False: 55.9525, -1: 44.835},
		2: {True: 28.8012, False: 58.4582, -1: 12.7406}
	}
}
not sure what is happening when O goes first… it should all be superficial… O or X going first doesn’t matter.
when both have the AI, the match is more contentious, and not a complete blowout, so that’s good.



after messing everything up...
added a method to use the max reward score from the reward matrix for a particular state
there’s something wrong with my second brain. a lot of the time all of the Q values for a particular state are 0 when they shouldn’t be.
{True: {True: {True: 91165, False: 2854, -1: 5981}, False: {True: 41484, False: 56008, -1: 2508}, -1: {True: 100000, False: 0, -1: 0}, 2: {True: 58240, False: 29026, -1: 12734}},
False: {True: {True: 55807, False: 41663, -1: 2530}, False: {True: 2583, False: 91008, -1: 6409}, -1: {True: 0, False: 100000, -1: 0}, 2: {True: 28981, False: 58326, -1: 12693}}}




changed the hyperparamters to include 50% epsilon/exploration, a million epoch, a learning rate of .1% and changed the input to a single brain
{True: {True: {True: 908700, False: 44236, -1: 47064}, False: {True: 320646, False: 679354, -1: 0}, -1: {True: 1000000, False: 0, -1: 0}, 2: {True: 585310, False: 287213, -1: 127477}}, False: {True: {True: 699247, False: 298628, -1: 2125}, False: {True: 31188, False: 906286, -1: 62526}, -1: {True: 0, False: 1000000, -1: 0}, 2: {True: 287881, False: 585318, -1: 126801}}}

changed the hyperparamters to include 40% epsilon/exploration, a million epoch, a learning rate of 1% and changed the input to a single brain
{True: {True: {True: 927172, False: 44317, -1: 28511}, False: {True: 308633, False: 691367, -1: 0}, -1: {True: 1000000, False: 0, -1: 0}, 2: {True: 584476, False: 288171, -1: 127353}}, False: {True: {True: 713045, False: 286955, -1: 0}, False: {True: 56934, False: 906619, -1: 36447}, -1: {True: 0, False: 1000000, -1: 0}, 2: {True: 288422, False: 584877, -1: 126701}}}


changed back to functions receiving training and using a single brain. need to remove the ‘first’ variable from most places as that was used to keep track of which brain to use/train…
epsilon = 20%, learning rate = 1%, epochs = 1 million, gamma is at .8 for this and all of the above
{True: {True: {True: 88699, False: 8522, -1: 2779}, False: {True: 36827, False: 61699, -1: 1474}, -1: {True: 100000, False: 0, -1: 0}, 2: {True: 58359, False: 28946, -1: 12695}}, False: {True: {True: 60966, False: 38229, -1: 805}, False: {True: 5374, False: 94364, -1: 262}, -1: {True: 0, False: 100000, -1: 0}, 2: {True: 28955, False: 58365, -1: 12680}}}


GAMMA = 0.8 LEARNING_RATE = .1 EPOCHS = 1000000 EPSILON = 0.3
{True: {True: {True: 861193, False: 59739, -1: 79068}, False: {True: 301057, False: 694752, -1: 4191}, -1: {True: 1000000, False: 0, -1: 0}, 2: {True: 584269, False: 288361, -1: 127370}}, False: {True: {True: 735289, False: 264711, -1: 0}, False: {True: 53021, False: 875489, -1: 71490}, -1: {True: 0, False: 1000000, -1: 0}, 2: {True: 288737, False: 585065, -1: 126198}}}


GAMMA = 0.8 LEARNING_RATE = 1 EPOCHS = 1000000 EPSILON = 0.1
{True: {True: {True: 704541, False: 163817, -1: 131642}, False: {True: 244260, False: 748078, -1: 7662}, -1: {True: 964760, False: 35240, -1: 0}, 2: {True: 584066, False: 288682, -1: 127252}}, False: {True: {True: 730362, False: 259539, -1: 10099}, False: {True: 176866, False: 693352, -1: 129782}, -1: {True: 13718, False: 986282, -1: 0}, 2: {True: 288537, False: 584432, -1: 127031}}}

GAMMA =  0.1 LEARNING_RATE = .001 EPOCHS = 1000000 EPSILON = 0.5
{True: {True: {True: 927358, False: 15494, -1: 57148}, False: {True: 300478, False: 694158, -1: 5364}, -1: {True: 1000000, False: 0, -1: 0}, 2: {True: 584630, False: 288553, -1: 126817}}, False: {True: {True: 732287, False: 263451, -1: 4262}, False: {True: 5264, False: 901021, -1: 93715}, -1: {True: 0, False: 1000000, -1: 0}, 2: {True: 288093, False: 584785, -1: 127122}}}


GAMMA =  0.1 LEARNING_RATE = .01 EPOCHS = 10000 EPSILON = 0.5

{True: {True: {True: 9603, False: 67, -1: 330}, False: {True: 950, False: 7692, -1: 1358}, -1: {True: 0, False: 10000, -1: 0}, 2: {True: 5819, False: 2910, -1: 1271}}, False: {True: {True: 7938, False: 869, -1: 1193}, False: {True: 28, False: 9625, -1: 347}, -1: {True: 0, False: 0, -1: 10000}, 2: {True: 2888, False: 5824, -1: 1288}}}

GAMMA =  0.1 LEARNING_RATE = .01 EPOCHS = 100000 EPSILON = 0.5

{True: {True: {True: 96038, False: 788, -1: 3174}, False: {True: 4743, False: 83903, -1: 11354}, -1: {True: 0, False: 0, -1: 100000}, 2: {True: 58391, False: 28942, -1: 12667}}, False: {True: {True: 79235, False: 6115, -1: 14650}, False: {True: 548, False: 96858, -1: 2594}, -1: {True: 0, False: 0, -1: 100000}, 2: {True: 28569, False: 58734, -1: 12697}}}

pickled brain:
GAMMA = .1
LEARNING_RATE = .01
EPOCHS = 10000000
EPSILON = 0.5
{True: {True: {True: 9483, False: 0, -1: 517}, False: {True: 335, False: 8537, -1: 1128}, -1: {True: 0, False: 0, -1: 10000}, 2: {True: 3550, False: 2881, -1: 3569}}, False: {True: {True: 8674, False: 327, -1: 999}, False: {True: 0, False: 9570, -1: 430}, -1: {True: 0, False: 0, -1: 10000}, 2: {True: 2899, False: 3607, -1: 3494}}}

It is possible to beat the AI when going second:

Do you want to be X's or O's?
x

Board State:
[0, 1, 2]
[3, 4, 5]
[6, 7, 8]

Board State:
['O', 1, 2]
[3, 4, 5]
[6, 7, 8]
The possible moves (0-8) are: [1, 2, 3, 4, 5, 6, 7, 8]
From the available positions where would you like to go?
The algorithm thinks you should go here: 7

8

Board State:
['O', 1, 2]
[3, 4, 5]
[6, 7, 'X']

Board State:
['O', 'O', 2]
[3, 4, 5]
[6, 7, 'X']
The possible moves (0-8) are: [2, 3, 4, 5, 6, 7]
From the available positions where would you like to go?
The algorithm thinks you should go here: 2

2

Board State:
['O', 'O', 'X']
[3, 4, 5]
[6, 7, 'X']

Board State:
['O', 'O', 'X']
[3, 4, 'O']
[6, 7, 'X']
The possible moves (0-8) are: [3, 4, 6, 7]
From the available positions where would you like to go?
The algorithm thinks you should go here: 6

6

Board State:
['O', 'O', 'X']
[3, 4, 'O']
['X', 7, 'X']

Board State:
['O', 'O', 'X']
[3, 'O', 'O']
['X', 7, 'X']
The possible moves (0-8) are: [3, 7]
From the available positions where would you like to go?
The algorithm thinks you should go here: 7

7
You won!
['O', 'O', 'X']
[3, 'O', 'O']
['X', 'X', 'X']
Would you like to play again?
 y / n ?
