class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
	    if all(coordinates[i + 1][0] - coordinates[i][0] == 0 for i in range(len(coordinates) - 1)):
		    return True
	    if coordinates[1][0] - coordinates[0][0] == 0:
		    return False
	    else:
		    k = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
		    for i in range(len(coordinates) - 1):
		    	if coordinates[i + 1][0] - coordinates[i][0] == 0:
		    		return False
		    	if (coordinates[i + 1][1] - coordinates[i][1]) / (coordinates[i + 1][0] - coordinates[i][0]) != k:
		    		return False
		    return True