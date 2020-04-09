# Description:
# Given an array of non-negative integers, you are initially positioned at the first index
# of the array.
# Each element in the array represents your maximum jump length at that position.
# Determine if you are able to reach the last index.

# Example 1:
# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
# Example 2:
# Input: [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum
#              jump length is 0, which makes it impossible to reach the last index.

from typing import List
class Solution:
	def canJump(self,nums: List[int]) -> bool:
		length = len(nums)
		# edge case
		if(length==0):
			return False
		if(length==1):
			return True
		# otherwise, use an int to store the furthest we can get from that index
		furthest = nums[0]
		for i in range(1,length):
			if(furthest>=i):
				furthest = max(furthest,i+nums[i])
		return (furthest >= length-1)

if __name__ == '__main__':
	soln = Solution()
	test1 = soln.canJump([]) #false
	test2 = soln.canJump([0]) #true
	test3 = soln.canJump([0,1]) #false
	test4 = soln.canJump([1,1,0]) #true
	test5 = soln.canJump([1,1,0,3]) #false
	test6 = soln.canJump([2,3,1,1,4]) #true
	test7 = soln.canJump([3,2,1,0,4]) #false

	assert test1 == 0
	assert test2 == 1
	assert test3 == 0
	assert test4 == 1
	assert test5 == 0
	assert test6 == 1
	assert test7 == 0
