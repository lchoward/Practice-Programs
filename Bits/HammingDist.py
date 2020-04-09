from typing import List

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        counter = 0 # use to count number of differing positions
        for i in range(32):
            x_i = (x>>i)&1
            y_i = (y>>i)&1
            counter += x_i ^ y_i
        return counter

if __name__ == '__main__':
    soln = Solution()
    test1 = soln.hammingDistance(1,4) #2
    test2 = soln.hammingDistance(0,7) #3
    test3 = soln.hammingDistance(15,16) #5

    assert test1 == 2
    assert test2 == 3
    assert test3 == 5