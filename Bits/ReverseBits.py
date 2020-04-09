# purpose: Reverse bits of a given 32 bits unsigned integer.
# e.g., 
# Input: 00000010100101000001111010011100
# Output: 00111001011110000010100101000000

from typing import List

class Solution:
    def reverseBits(self, n: int) -> int:
        reversedInt = 0

        # go through each bit and OR it to the answer
        for i in range(32):
        	currentBit = (n >> i) & 1
        	reversedInt |= (currentBit << (31-i))

        return reversedInt

if __name__ == '__main__':
	soln = Solution()
	test1 = soln.reverseBits(43261596) # should be 964176192
	test2 = soln.reverseBits(4294967293) # should be 3221225471

	assert test1 == 964176192
	assert test2 == 3221225471