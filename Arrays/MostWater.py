# purpose: Given n non-negative integers a1, a2, ..., an , where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i
# is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container,
# such that the container contains the most water.

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # idea: run one pointer from far left and one from far right
        # only adjust the pointer toward the middle if it is shorter than the other
        # update max volume if required

        numLines = len(height)

        # corner cases
        if (numLines  < 2):
            return 0
        if (numLines == 2):
            return (min(height[0],height[1]))

        # normal cases
        else:
            maximumArea = 0
            front = 0 # index closer to the far left
            back = numLines-1 # index closer to the far right
            while(front < back):
                currWidth = back - front 
                if (height[front] >= height[back]):
                    shorterLine = height[back]
                    currArea = currWidth * shorterLine
                    back -= 1
                else:
                    shorterLine = height[front]
                    currArea = currWidth * shorterLine
                    front += 1
                if (currArea > maximumArea):
                    maximumArea = currArea
            return maximumArea

if __name__ == '__main__':
    soln = Solution()
    test1 = soln.maxArea([]) #should return 0
    test2 = soln.maxArea([1]) #should return 0
    test3 = soln.maxArea([0,0]) #should return 0
    test4 = soln.maxArea([1,2,3]) # should return 2
    test5 = soln.maxArea([4,5,6,6,5,4]) # should return 20

    assert test1 == 0, "test1 failed"
    assert test2 == 0, "test2 failed"
    assert test3 == 0, "test3 failed"
    assert test4 == 2, "test4 failed"
    assert test5 == 20, "test5 failed"