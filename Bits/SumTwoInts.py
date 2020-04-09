# purpose: Calculate the sum of two integers a and b, but you are not allowed to use the
# operator + and -.

from typing import List

class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        sum = 0

        for i in range(32):
            a_i = (a >> i) & 1 # get the ith bit of a
            b_i = (b >> i) & 1 # get the ith bit of b
            sum_i = a_i ^ b_i ^ carry # get the ith bit of the sum
            sum |= (sum_i << i) # add the ith bit to sum
            carry = (a_i & b_i) | (a_i ^ b_i) & carry

        # print("sum is: " + str(sum))

        # case 1: positive
        if (sum < pow(2,31)):
            return sum
        # case 2: negative
        else:
            return sum - pow(2,32)


if __name__ == '__main__':
    soln = Solution()
    test1 = soln.getSum(1,-1) # should be 0
    test2 = soln.getSum(20,50) # should be 70
    test3 = soln.getSum(-20,5) # should be -15
    test4 = soln.getSum(-200, -200) # should be -400

    assert test1 == 0, "test1 failed"
    assert test2 == 70, "test2 failed"
    assert test3 == -15, "test3 failed"
    assert test4 == -400, "test4 failed"