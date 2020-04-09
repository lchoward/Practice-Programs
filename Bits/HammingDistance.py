# Return the number of positions at which two ints' bits are different

class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        res = 0
        for i in range(32):
            a = (x >> i) & 1
            b = (y >> i) & 1
            res += a ^ b
        return res