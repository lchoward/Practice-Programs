# Description
# You are a professional robber planning to rob houses along a street. Each house has a
# certain amount of money stashed. All houses at this place are arranged in a circle. That
# means the first house is the neighbor of the last one. Meanwhile, adjacent houses have
# security system connected and it will automatically contact the police if two adjacent
# houses were broken into on the same night.

# Given a list of non-negative integers representing the amount of money of each house,
# determine the maximum amount of money you can rob tonight without alerting the police.

# Example 1:

# Input: [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
#              because they are adjacent houses.
# Example 2:

# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.

# [9,2,5,2,1,11,9,9]
# [9,2,14,11,15,25,24,25]
# [T,F,T,T,T,T,T,T]
# [20,2,13,4,14,24,23,100]
# [20T,2F,33T,24T,57T,56T,137]

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        numNums = len(nums)
        # edge cases
        if(numNums == 0):
            return 0
        elif(numNums<=3):
            return max(nums)
        elif(numNums==4):
            return max(nums[0]+nums[2],nums[1]+nums[3])

        def max_Amt(homes: List[int]) -> int:
            numHomes = len(homes)
            # initialize for 3rd home
            homes[2] += homes[0]
            for i in range(3,numHomes):
                homes[i] += max(homes[i-3],homes[i-2])
            return max(homes[-1],homes[-2])
        # since we can't use both the first and last home, we'll run one w/ and one w/o
        return max(max_Amt(nums[:-1]),max_Amt(nums[1:]))

        

if __name__ == '__main__':
    soln = Solution()
    test1 = soln.rob([]) #0
    test2 = soln.rob([1]) #1
    test3 = soln.rob([1,2]) #2
    test4 = soln.rob([1,2,3]) #3
    test5 = soln.rob([1,2,1,2]) #4
    test6 = soln.rob([3,2,1,4,6]) #8
    test7 = soln.rob([20,2,13,4,14,24,23,100]) #137
    test8 = soln.rob([4,1,2,7,5,3,1]) #14
    test9 = soln.rob([2,1,2,6,1,8,10,10]) #25

    assert test1 == 0
    assert test2 == 1
    assert test3 == 2
    assert test4 == 3
    assert test5 == 4
    assert test6 == 8
    assert test7 == 137
    assert test8 == 14
    assert test9 == 25
