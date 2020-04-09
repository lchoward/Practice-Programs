# Given a m x n matrix, if an element is 0, set its entire row and column to 0.
# Do it in-place.
#
# Example 1:
# Input: 
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# Output: 
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
#
# Example 2:
# Input: 
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# Output: 
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]
#
# Follow up:
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?

# approach:
# (1) go through matrix, find all 0's
# (2) store all row vals in set1, col vals in set2
# (3) for all vals in hashmap1, set those rows to 0
# (4) for all vals in hashmap2, set those cols to 0

class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None
        """
        if matrix == []:
            return
        rows, cols = len(matrix), len(matrix[0])

        set1, set2 = set(), set()

        # find all 0's
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    set1.add(i)
                    set2.add(j)

        # iterate through hashmaps and set 0's
        for row in list(set1):
            for j in range(cols):
                matrix[row][j] = 0

        for col in list(set2):
            for i in range(rows):
                matrix[i][col] = 0

        return










