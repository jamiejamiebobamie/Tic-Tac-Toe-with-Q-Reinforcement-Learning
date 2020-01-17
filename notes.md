# Results from training_and_validation.py
{
 ## True: 														// X went first.
	 {	True: {True: 80384, False: 8723, -1: 10893}, 		// X has the AI - > X won 80.384%
		False: {True: 39732, False: 52727, -1: 7541},		// O has the AI - > O won 52.727%
		-1: {True: 71552, False: 20298, -1: 8150},		// both have the AI - > X won 71.552%		
		2: {True: 58246, False: 28915, -1: 12839}		// neither has the AI - > X won 58.246%
	 },
## False: 														// O went first
	 {	True: {True: 53031, False: 39481, -1: 7488}, 		// X has the AI - > X won 53.031%
		False: {True: 8441, False: 79741, -1: 11818},		// O has the AI - > O won 79.741%
		-1: {True: 19397, False: 72016, -1: 8587},		// both have the AI - > O won 72.016%		
		2: {True: 29024, False: 58184, -1: 12792}		// neither has the AI - > O won 58.184%
	 }
}
## every time the trained ai was playing an ai that was picking at random and won.
## (80,384 + 52,727 + 53,031 + 79,741) = 265, 883
##
## every time the trained ai was playing an ai that was picking at random and lost.
## (8723 + 39732 + 39481 + 8441) = 96,377
##
## every time the trained ai was playing an ai that was picking at random and tied.
## (10893 + 11818 + 7488 + 7541) = 37,740
##
## 66% accuracy
## the AI wins 2/3rds of the games it plays, regardless of who goes first.
