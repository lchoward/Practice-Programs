# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix
# in spiral order.
#
# Example 1:
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
#
# Example 2:
# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# approach:
# (1) use pointer for row and column
# (2) traverse matrix by going far right, far down, far left, far up
# (3) note: on each right, you can go til end of row
#           on each down, you can go til bottom of col
#           on each left, you can go til front of row
#           on each up, you can go to top of col - 1
#           next right goes row - 1
#           next down goes col - 1
#           etc
# (4) terminate if you start where you are supposed to end on a new direction
#     e.g., start going right, but i == end of row
#           start going down, but j == bottom of col
#           start going left, but i == front of row
#           start going down, but j == top of col

class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        rows, cols = len(matrix), len(matrix[0])

        # edge case for 1 row or 1 column
        if rows == 1:
            return matrix[0]
        if cols == 1:
            res = []
            for i in range(rows):
                res.append(matrix[i][0])
            return res

        # all other cases
        l, r, t, b = 0, rows, 0, cols # left, right, top, bottom constraints
        i, j = 0, 0 # use i as pointer for row, j for col
        direction = 0 # (0 = right, 1 = down, 2 = left, 3 = up)
        res = []

        # begin spiraling from top left (matrix[0][0])
        while True:
            if direction == 0:
                if j > r: return res
                for j in range(j, r):
                    res.append(matrix[i][j])
                t += 1 # increment top since we just went through it
                i += 1
                direction = 1
            if direction == 1:
                if i > b: return res
                for i in range(i, b):
                    res.append(matrix[i][j])
                r -= 1 # decrement right since we just went through it
                j -= 1
                direction = 2
            if direction == 2:
                if j < l: return res
                for j in range(j, l - 1, -1):
                    res.append(matrix[i][j])
                b -= 1 # decrement botttom since we just went through it
                i -= 1
                direction = 3
            if direction == 3:
                if i < t: return res
                for i in range(i, t - 1, -1):
                    res.append(matrix[i][j])
                l += 1 # increment left since we just went through it
                j += 1
                direction = 0

if __name__ == '__main__':
    soln = Solution()
    test1 = soln.spiralOrder([]) #[]
    test2 = soln.spiralOrder([[1,2]]) #[1,2]
    test3 = soln.spiralOrder([[1],[2],[3],[4]]) #[1,2,3,4]
    test4 = soln.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) #[1,2,3,6,9,8,7,4,5]
    test5 = soln.spiralOrder([[1,2],[3,4]]) #[1,2,4,3]
    test6 = soln.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) #[1,2,3,4,8,12,11,10,9,5,6,7]

    assert test1 == []
    assert test2 == [1,2]
    assert test3 == [1,2,3,4]
    assert test4 == [1,2,3,6,9,8,7,4,5]
    assert test5 == [1,2,4,3]
    print(test6)







