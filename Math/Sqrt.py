# Implement int sqrt(int x).
# Compute and return the square root of x, where x is guaranteed to be a non-negative
# integer.
# Since the return type is an integer, the decimal digits are truncated and only the
# integer part of the result is returned.
#
# Example 1:
# Input: 4
# Output: 2
#
# Example 2:
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since 
#              the decimal part is truncated, 2 is returned.

# approach:
# (1) use left and right pointers to conduct a sort of binary search
# (2) only difference is we maintain a refernce to the maximum number that has worked ...
# (3) ... as well as a reference the minimum number that has not worked

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # corner cases / bad inputs
        if x == 0:
            return 0

        if x < 0:
            return -2147483648

        l, r = 1, 1
        maximum, minimum = 0, x + 1
        while maximum < minimum - 1:
            if r * r <= x:
                maximum = r
                l = r
                r = min(2 * r, int((minimum + l) / 2))
            else:
                minimum = r
                r = int((l + r) / 2)

        return maximum

if __name__ == '__main__':
    soln = Solution()
    test1 = soln.mySqrt(1) # 1
    test2 = soln.mySqrt(0) # 0
    test3 = soln.mySqrt(2) # 1
    test4 = soln.mySqrt(16) # 4
    test5 = soln.mySqrt(190) # 13
    test6 = soln.mySqrt(492280) # 701
    test7 = soln.mySqrt(123456789) # 11111
    test8 = soln.mySqrt(9) # 3

    assert test1 == 1
    assert test2 == 0
    assert test3 == 1
    assert test4 == 4
    assert test5 == 13
    assert test6 == 701
    assert test7 == 11111
    assert test8 == 3







