# purpose: Given an unsorted array of integers, find the length of longest increasing
# subsequence.

from typing import List

class Solution:
	def lengthOfLIS(self, nums: List[int]) -> int:
		listLen = len(nums)
		# corner case
		if(listLen <= 1):
			return listLen

		# otherwise, proceed to main code
		longest = [1] * (listLen) # use longest[i] to store the longest LIS at nums[i]

		for currNum in range(1,listLen):
			for prevNum in range(currNum):
				if(nums[prevNum] < nums[currNum]):
					longest[currNum] = max(longest[currNum],longest[prevNum]+1)
		return (max(longest))

if __name__ == '__main__':
	soln = Solution()
	test1 = soln.lengthOfLIS([]) # should be 0
	test2 = soln.lengthOfLIS([1]) # should be 1
	test3 = soln.lengthOfLIS([1,2,3]) # should be 3
	test4 = soln.lengthOfLIS([10,9,11,12,2,5,3,7,10]) # should be 4
	test5 = soln.lengthOfLIS([10,9,11,12,2,5,3,7,10,3,4,5,6]) # should be 5

	assert test1 == 0
	assert test2 == 1
	assert test3 == 3
	assert test4 == 4
	assert test5 == 5