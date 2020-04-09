# purpose: Given an array nums of n integers where n > 1,  return an array output such that
# output[i] is equal to the product of all the elements of nums except nums[i]

# Note: must run in O(n) w/o dividing

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        inputLen = len(nums)
        # initialize output array to all 1s
        output = [1] * inputLen
        # multiply each number from left to right, starting at the second
        for i in range(1, inputLen):
            output[i] = output[i-1] * nums[i-1]

        # multiply from right to left
        multiplier = 1
        for i in range(inputLen-1,-1,-1):
            #print("i is: " + str(i))
            output[i] = output[i] * multiplier
            multiplier *= nums[i]

        #print(output)
        return output

if __name__ == '__main__':
    soln = Solution()
    test1 = soln.productExceptSelf([1,2,3,4]) # output should be [24,12,8,6]

    assert test1 == [24,12,8,6], "Test 1 failed"

