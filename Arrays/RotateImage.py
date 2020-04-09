# You are given an n x n 2D matrix representing an image.
# Rotate the image by 90 degrees (clockwise).
# Note:
# You have to rotate the image in-place, which means you have to modify the input 2D matrix
# directly. DO NOT allocate another 2D matrix and do the rotation.

from math import ceil

class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        :type matrix: List[List[int]]
        :rtype: None
        """
        n = len(matrix)
        if not matrix:
            return
        
        i_loop = math.ceil(n / 2) - n % 2 # to account for odd n's (e.g., 3)
        j_loop = math.ceil(n / 2)
        
        for i in range(i_loop):
            for j in range(j_loop):
                temp = matrix[i][j]
                matrix[i][j]         = matrix[n-1-j][i]
                matrix[n-1-j][i]     = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i]     = temp
        return