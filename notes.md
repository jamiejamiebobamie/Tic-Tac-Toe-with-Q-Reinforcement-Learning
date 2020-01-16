# Results from training_and_validation:
## using test_Q_with_state_max() method
##    in the unit_test() method of test_accuracy()
### {
### True:
	### {	### True: {True: 43330, False: 42922, -1: 13748},
		### False: {True: 75028, False: 6678, -1: 18294},
		### -1: {True: 67142, False: 11259, -1: 21599},
		### 2: {True: 58506, False: 28856, -1: 12638}
	### },
### False:
	### {	### True: {True: 6530, False: 75178, -1: 18292},
		### False: {True: 42984, False: 43357, -1: 13659},
		### -1: {True: 12599, False: 66399, -1: 21002},
		### 2: {True: 28874, False: 58378, -1: 12748}
	### }
### }
## using test_Q_with_state() method
##    in the unit_test() method of test_accuracy()
### {
### True: 														### // X went first.
	### {	### True: {True: 80384, False: 8723, -1: 10893}, 		### // X has the AI - > ( won 80384 out of ( 80384 + 8723 + 10893 ) )
		### False: {True: 39732, False: 52727, -1: 7541},		### // O has the AI - > ( won 52727 out of ( 52727 + 39732 + 7541 ) )
		### -1: {True: 71552, False: 20298, -1: 8150},
		### 2: {True: 58246, False: 28915, -1: 12839}
	### },
### False: 														### // O went first
	### {	### True: {True: 53031, False: 39481, -1: 7488}, 		### // X has the AI - > ( won 53031 out of ( 53031 + 39481 + 7488 ) )
		### False: {True: 8441, False: 79741, -1: 11818},		### // O has the AI - > ( won 79741 out of ( 79741 + 8441 + 11818 ) )
		### -1: {True: 19397, False: 72016, -1: 8587},
		### 2: {True: 29024, False: 58184, -1: 12792}
	### }
### }
