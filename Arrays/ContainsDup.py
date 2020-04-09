# purpose: determine if there is a duplicate value in a list of integers

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        arrLength = len(nums)
        if (arrLength < 2):
            return False
        else:
            for i in range (0, arrLength - 1):
                if (nums[i] == nums[i+1]):
                    return True
            return False

if __name__ == '__main__':
    soln = Solution()
    test1 = soln.containsDuplicate([0,1,2,3,4])
    test2 = soln.containsDuplicate([-1,0,4,5,10,-1])
    test3 = soln.containsDuplicate([])
    test4 = soln.containsDuplicate([1,])
    test5 = soln.containsDuplicate([0,1,2,3,4,10,10])

    assert test1 == False, "this should be false"
    assert test2 == True, "this should be true"
    assert test3 == False, "this should be false"
    assert test4 == False, "this should be false"
    assert test5 == True, "this should be true"
    print("Testing is done.")