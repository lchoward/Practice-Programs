# 1,2,3 = you win
# 4,8,12 = lose
# 5 = you win
# 6 = you win

from typing import List

class Solution:
    def canWinNim(self, n: int) -> bool:
    	if(n % 4) == 0:
    		return False
    	else:
    		return True

if __name__ == '__main__':
	soln = Solution()
	test1 = soln.canWinNim(1) #True
	test2 = soln.canWinNim(2) #True
	test3 = soln.canWinNim(3) #True
	test4 = soln.canWinNim(4) #False
	test5 = soln.canWinNim(5) #True
	test6 = soln.canWinNim(6) #True
	test7 = soln.canWinNim(7) #True
	test8 = soln.canWinNim(8) #False

	assert test1 == True
	assert test2 == True
	assert test3 == True
	assert test4 == False
	assert test5 == True
	assert test6 == True
	assert test7 == True
	assert test8 == False