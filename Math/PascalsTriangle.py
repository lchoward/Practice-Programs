# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        res = [None] * numRows
        res[0] = [1]
        
        # iterate through next rows
        for i in range(1, numRows):
            for j in range(i + 1):
                if j == 0:
                    res[i] = [1]
                elif j == i:
                    res[i].append(1)
                else:
                    res[i].append(res[i-1][j-1]+res[i-1][j])
        return res