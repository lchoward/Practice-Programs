# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.
#
# Example:
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#
# Follow up:
# If you have figured out the O(n) solution, try coding another solution using the divide
# and conquer approach, which is more subtle.

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        arr = [float('-inf')] * length
        arr[0], maximum = nums[0], nums[0]
        for i in range(1, length):
            if arr[i - 1] + nums[i] > nums[i]:
                arr[i] = arr[i - 1] + nums[i]
            else:
                arr[i] = nums[i]
            if arr[i] > maximum:
                maximum = arr[i]
        return maximum