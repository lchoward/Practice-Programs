# Given an m x n matrix of non-negative integers representing the height of each unit
# cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix
# and the "Atlantic ocean" touches the right and bottom edges.

# Water can only flow in four directions (up, down, left, or right) from a cell to another
# one with height equal or lower.

# Find the list of grid coordinates where water can flow to both the Pacific and Atlantic
# ocean.

# Note:

# The order of returned grid coordinates does not matter.
# Both m and n are less than 150.
 

# Example:

# Given the following 5x5 matrix:

#   Pacific ~   ~   ~   ~   ~ 
#        ~  1   2   2   3  (5) *
#        ~  3   2   3  (4) (4) *
#        ~  2   4  (5)  3   1  *
#        ~ (6) (7)  1   4   5  *
#        ~ (5)  1   1   2   4  *
#           *   *   *   *   * Atlantic

# Return:

# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
# (positions with parentheses in above matrix).

from typing import List
from collections import deque

class Solution:
	# function for BFS
	def bfs(self, dq, matrix, visited):
		N, M = len(matrix), len(matrix[0])
		while dq:
			(x,y) = dq.popleft()
			nextCells = [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]
			for (x1,y1) in nextCells:
				if (0<=x1<N and 0<=y1<M and not visited[x1][y1]
				and matrix[x1][y1] >= matrix[x][y]):
				    dq.append((x1,y1))
				    visited[x1][y1] = True
		return

	# function to initialize the dq's and visited matrices
	def initialize_dq(self, N, M, pac_dq, atl_dq, pac_visited, atl_visited):
		for i in range(N):
			pac_dq.append((i, 0))
			atl_dq.append((i, M-1))
			pac_visited[i][0], atl_visited[i][M-1] = True, True

		for j in range(M):
			pac_dq.append((0, j))
			atl_dq.append((N-1, j))
			pac_visited[0][j], atl_visited[N-1][j] = True, True
		return

	def pacificAtlantic(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[List[int]]
		"""

		if matrix == []:
			return []

		# initialize the dq
		N, M = len(matrix), len(matrix[0])
		pac_dq, atl_dq = deque(), deque()
		pac_visited = [[False]*M for _ in range(N)]
		atl_visited = [[False]*M for _ in range(N)]
		self.initialize_dq(N, M, pac_dq, atl_dq, pac_visited, atl_visited)

		# call bfs on both oceans
		self.bfs(pac_dq, matrix, pac_visited)
		self.bfs(atl_dq, matrix, atl_visited)

		# check for cells that are True on both oceans and append to result
		output = []
		for i in range(N):
			for j in range(M):
				if pac_visited[i][j] and atl_visited[i][j]:
					output.append([i,j])
		return output

if __name__ == '__main__':
	soln = Solution()
	test1 = soln.pacificAtlantic([]) # []
	test2 = soln.pacificAtlantic([[0,0],[0,0]]) # [[0,0],[0,1],[1,0],[1,1]]