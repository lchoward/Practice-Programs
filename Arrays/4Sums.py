# purpose: return unique quadtuples of an array that add to the target number
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        inputLen = len(nums)
        # check for invalid input
        if (inputLen < 4):
            return[]
        solution = [[]]

        # sort the array to simplify our lives
        nums.sort()
        print(nums)
        
        # run 4 pointers to scan through the array
        for i in range(0, inputLen-3):
            # break if the target is out of reach (4x the largest / smallest number)
            if (target < 4 * nums[i] or target > 4 * nums[inputLen-1]):
                break
            # continue to avoid duplicates
            if (i > 0 and nums[i] == nums[i-1]):
                continue
            for j in range(i+1,inputLen-2):
                sum3 = target - nums[i]
                # break if the target is out of reach again (3x)
                if (sum3 < 3 * nums[j] or sum3 > 3 * nums[inputLen-1]):
                    break
                sum2 = target - nums[i] - nums[j]
                
                # use two pointers to scan now, one going from front and one from back
                front = j+1
                back = inputLen-1
                while (front < back):
                    # break if the target is out of reach again (2x)
                    if (sum2 < 2 * nums[front] or sum2 > 2 * nums[back]):
                        break
                    if (nums[front] + nums[back] == sum2):
                        currList = [nums[i], nums[j], nums[front], nums[back]]
                        front += 1
                        back -= 1
                        if (not(currList in solution)):
                            solution.append(currList)
                    elif (nums[front] + nums[back] > sum2):
                        back -= 1
                    else:
                        front += 1
        solution.remove([])
        return solution

if __name__ == '__main__':
    # run a test on something easy
    test1 = Solution()
    output1 = test1.fourSum([0,1,2,3,2,1,0,-1,-2,-3], 0)
    print(str(output1))