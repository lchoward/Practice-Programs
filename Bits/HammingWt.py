# purpose: Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).

from typing import List

class Solution:
    def hammingWeight(self, n: int) -> int:
    	numOnes = 0
    	for i in range(32):
    		numOnes += (n >> i) & 1
    	return numOnes

if __name__ == '__main__':
	soln = Solution()
	test1 = soln.hammingWeight(7) # should be 3
	test2 = soln.hammingWeight(0) # should be 0
	test3 = soln.hammingWeight(8) # should be 1
	test4 = soln. hammingWeight(15) # should be 4

	assert test1 == 3, "test1 failed"
	assert test2 == 0, "test2 failed"
	assert test3 == 1, "test3 failed"
	assert test4 == 4, "test4 failed"