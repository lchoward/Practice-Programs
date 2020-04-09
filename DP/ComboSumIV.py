# Description:
# Given an integer array with all positive numbers and no duplicates, find the number of
# possible combinations that add up to a positive integer target.

# Example:
# Inputs: nums = [1, 2, 3]; target = 4

# Answer: The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# Note that different sequences are counted as different combinations.
# Therefore the output is 7.

from typing import List

class Solution:
	def combinationSum4(self, nums: List[int], target: int) -> int:
		lenNums = len(nums)
		# check for bad inputs
		if (lenNums == 0 or target <= 0):
			return 0

		# numWays[i] shows how many ways we have to sum to i using our nums
		numWays = [0] * (target+1)
		# initialize with the nums we have
		for num in nums:
			if(num <= target):
				numWays[num] = 1

		nums.sort()

		for i in range(target+1):
			for num in nums:
				currVal = i - num
				if (currVal >= 1):
					numWays[i] += numWays[currVal]

		return numWays[target]

if __name__ == '__main__':
	soln = Solution()
	test1 = soln.combinationSum4([],1) #0
	test2 = soln.combinationSum4([1],0) #0
	test3 = soln.combinationSum4([1,2,3],2) #2
	test4 = soln.combinationSum4([1,2,3],4) #7
	test5 = soln.combinationSum4([1,2,3],5) #13

	assert test1 == 0
	assert test2 == 0
	assert test3 == 2
	assert test4 == 7
	assert test5 == 13