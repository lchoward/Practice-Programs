# background: You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Note: Given n will be a positive integer.

from typing import List

class Solution:
	def climbStairs(self, n: int) -> int:
		# check for bad inputs
		if (n <= 0):
			return 0

		# base cases n=1 and n=2
		if (n == 1):
			return 1

		if (n == 2):
			return 2

		# all other cases:

		else:
			# start the memo
			memo = [0]*(n+1)
			memo[1] = 1
			memo[2] = 2
			for i in range(3,n+1):
				memo[i] = memo[i-1] + memo[i-2]
			return memo[n]

if __name__ == '__main__':
	soln = Solution()
	test1 = soln.climbStairs(0) #should be 0
	test2 = soln.climbStairs(1) #should be 1
	test3 = soln.climbStairs(2) #should be 2
	test4 = soln.climbStairs(3) #should be 3
	test5 = soln.climbStairs(4) #should be 5
	test6 = soln.climbStairs(5) #should be 8

	assert test1 == 0
	assert test2 == 1
	assert test3 == 2
	assert test4 == 3
	assert test5 == 5
	assert test6 == 8