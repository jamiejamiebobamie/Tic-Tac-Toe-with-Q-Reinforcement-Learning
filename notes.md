# using test_Q_with_state (_min) in the unit test < — works! (at least better than picking randomly)
## {
 ## True: 														// X went first.
	 {	True: {True: 80384, False: 8723, -1: 10893}, 		// X has the AI - > X won 80.384%
		 False: {True: 39732, False: 52727, -1: 7541},		// O has the AI - > O won 52.727%
		 -1: {True: 71552, False: 20298, -1: 8150},			// both have the AI - > X won 71.552%		
		 2: {True: 58246, False: 28915, -1: 12839}			// neither has the AI - > X won 58.246%
	 },
## False: 														// O went first
	 {	True: {True: 53031, False: 39481, -1: 7488}, 		// X has the AI - > X won 53.031%
		 False: {True: 8441, False: 79741, -1: 11818},		// O has the AI - > O won 79.741%
		 -1: {True: 19397, False: 72016, -1: 8587},			// both have the AI - > O won 72.016%		
		 2: {True: 29024, False: 58184, -1: 12792}			// neither has the AI - > O won 58.184%
	 }
## }
