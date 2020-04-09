# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
# An island is surrounded by water and is formed by connecting adjacent lands horizontally
# or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input:
# 11110
# 11010
# 11000
# 00000

# Output: 1

# Example 2:

# Input:
# 11000
# 11000
# 00100
# 00011

# Output: 3

from collections import deque

class Solution:
    # bfs on 1's
    def check_islands(self, dq, grid, visited, counter):
        N, M = len(grid), len(grid[0])
        while dq:
            (x,y) = dq.popleft()
            visited[x][y] = True
            adjacents = [(x-1,y), (x,y-1), (x+1,y), (x,y+1)]
            for (x1,y1) in adjacents:
                if (0<=x1<N and 0<=y1<M and grid[x1][y1] == '1' and
                    not visited[x1][y1]):
                    counter -= 1
                    dq.appendleft((x1,y1))
                    visited[x1][y1] = True

        return counter

    # initialize the numbers matrix corresponding to islands
    def initialize_islands(self, N, M, dq, grid):
        counter = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j] == '1':
                    counter += 1
                    dq.append((i, j))
        return counter

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        if grid == []:
            return 0

        N, M = len(grid), len(grid[0])
        dq = deque()
        visited = [[False]*M for _ in range(N)]

        init = self.initialize_islands(N, M, dq, grid)
        final = self.check_islands(dq, grid, visited, init)

        return final


if __name__ == '__main__':
    soln = Solution()
    test1 = soln.numIslands([]) #0

    test2 = soln.numIslands([["1","1","1","1","0"],
                             ["1","1","1","1","0"],
                             ["1","1","1","1","0"],
                             ["1","1","1","1","0"],
                             ["1","1","1","1","0"]]) #1

    test3 = soln.numIslands([["1","1","0","1","0"],
                             ["1","1","0","1","0"],
                             ["0","0","0","1","0"],
                             ["1","1","0","1","0"],
                             ["1","1","0","1","0"]]) #3

    test4 = soln.numIslands([["1","1","0"],
                             ["0","1","0"],
                             ["1","1","1"]]) #1

    assert test1 == 0
    assert test2 == 1
    assert test3 == 3
    assert test4 == 1



