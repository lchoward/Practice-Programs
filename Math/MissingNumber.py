# Determine the missing number from the list [0, 1, 2, ..., n]
# Assume valid input, e.g., if nums is length n, then one element between 0 and n 
# (inclusive) is missing

class Solution:
    def missingNumber(self, nums):
    	"""
    	:type nums: List[int]
    	:rtype: int
    	"""
        length = len(nums)
        if length == 0:
            return 0
        sum = int(length * (length + 1) / 2)
        for num in nums:
            sum -= num
        return sum