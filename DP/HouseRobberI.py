# Description:
# You are a professional robber planning to rob houses along a street. Each house has a
# certain amount of money stashed, the only constraint stopping you from robbing each of
# them is that adjacent houses have security system connected and it will automatically
# contact the police if two adjacent houses were broken into on the same night.

# Given a list of non-negative integers representing the amount of money of each house,
# determine the maximum amount of money you can rob tonight without alerting the police.

# Example 1:
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.
# Example 2:

# Input: [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
#              Total amount you can rob = 2 + 9 + 1 = 12.


from typing import List

class Solution:
	def rob(self, nums: List[int]) -> int:
		numHomes = len(nums)

		# edge cases for less than 4 homes
		if(numHomes == 0):
			return 0
		elif(numHomes == 1):
			return nums[0]
		elif(numHomes == 2):
			return max(nums)
		elif(numHomes == 3):
			return max(nums[0]+nums[2],nums[1])

		# for 4 or more homes
		amount = [0] * (numHomes) # amount[i] is the max you can have at house i
		amount[0] = nums[0]
		amount[1] = nums[1]
		amount[2] = nums[0]+nums[2]
		for i in range(3,numHomes):
			bestVal = max(amount[i-2],amount[i-3])
			amount[i] = bestVal + nums[i]

		return max(amount[numHomes-1],amount[numHomes-2])

if __name__ == '__main__':
	soln = Solution()
	test1 = soln.rob([2,7,9,3,1]) #12
	test2 = soln.rob([]) #0
	test3 = soln.rob([1]) #1
	test4 = soln.rob([1,2]) #2
	test5 = soln.rob([1,5,3]) #5
	test6 = soln.rob([1,2,3,1]) #4
	test7 = soln.rob([1,5,1,1,10,3,1,20]) #35

	assert test1 == 12
	assert test2 == 0
	assert test3 == 1
	assert test4 == 2
	assert test5 == 5
	assert test6 == 4
	assert test7 == 35

