# Description:
# A robot is located at the top-left corner of a m x n grid
# The robot can only move either down or right at any point in time. The robot is trying to
# reach the bottom-right corner of the grid.
# How many possible unique paths are there?
# Note: m and n will be at most 100.

# Example 1:
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right
#
# Example 2:
# Input: m = 7, n = 3
# Output: 28

from typing import List

class Solution:
	def uniquePaths(self, m: int, n: int) -> int:
		#edge cases
		if (m<=0 or n<=0):
			return 0
		elif (m==1 or n==1):
			return 1

		#create a m by n grid; 0,0 will be end; (m-1),(n-1) will be start
		grid=[]
		for i in range(m):
			grid.append([0]*n)
		# initialize all of grid[0][n] and grid[m][0] to 1
		for i in range(n):
			grid[0][i] = 1
		for i in range(m):
			grid[i][0] = 1

		# for all other spots, grid[i][j] = grid[i-1][j] + grid[i][j-1]
		for i in range(1,m):
			for j in range(1,n):
				grid[i][j] = grid[i-1][j] + grid[i][j-1]

		return grid[m-1][n-1]

if __name__ == '__main__':
	soln = Solution()
	test1 = soln.uniquePaths(5,0) #0
	test2 = soln.uniquePaths(0,5) #0
	test3 = soln.uniquePaths(1,5) #1
	test4 = soln.uniquePaths(3,2) #3
	test5 = soln.uniquePaths(2,3) #3
	test6 = soln.uniquePaths(7,3) #28
	test7 = soln.uniquePaths(3,7) #28

	assert test1 == 0
	assert test2 == 0
	assert test3 == 1
	assert test4 == 3
	assert test5 == 3
	assert test6 == 28
	assert test7 == 28
