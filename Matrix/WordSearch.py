# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent"
# cells are those horizontally or vertically neighboring. The same letter cell may not be
# used more than once.
#
# Example:
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
#
# Constraints:
# board and word consists only of lowercase and uppercase English letters.
# 1 <= board.length <= 200
# 1 <= board[i].length <= 200
# 1 <= word.length <= 10^3

# approach:
# (1) dfs from board[0][0] to board[rows-1][cols-1]
# (2) check each neighbor (make sure not to go out of bounds; don't go to ones already in)
# (3) if any neighbor has next letter, continue the search from there
# (4) otherwise, break and go back to last spot

class Solution:
	def exist(self, board, word):
		"""
		:type board: List[List[str]]
		:type word: str
		:rtype: bool
		"""
		# check for bad inputs
		if not board or not word:
			return False
		rows, cols = len(board), len(board[0])
		letters = len(word)

		# check for longer word than board
		if letters > rows * cols:
			return False

		neighbors = [(0,1),(1,0),(0,-1),(-1,0)]

		# helper functiont to perform dfs
		def dfs(board, word, x, y, streak, count):
			if count == letters:
				# print("x is: %s, y is: %s" % (x,y))
				return True
			for (x1,y1) in neighbors:
				x2, y2 = x + x1, y + y1
				if 0 <= x2 < rows and 0 <= y2 < cols and (x2, y2) not in streak:
					if board[x2][y2] == word[count]:
						streak.add((x2, y2))
						check = dfs(board, word, x2, y2, streak, count + 1)
						if check:
							return True
						else:
							streak.remove((x2, y2))
			return False

		# call dfs on all cells in board
		for i in range(rows):
			for j in range(cols):
				if board[i][j] == word[0]:
					streak = {(i, j)}
					check = dfs(board, word, i, j, streak, 1)
					if check:
						# print("i is: %s, j is: %s" % (i,j))
						return True
		return False

if __name__ == '__main__':
	soln = Solution()
	test1 = soln.exist([],"hello") #false
	test2 = soln.exist([["A","B"]],"") #false
	test3 = soln.exist([["A","B","C"]],"CBA") #true
	test4 = soln.exist([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']],"SEE") #true
	test5 = soln.exist([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']],"BFDECCESE") #true
	test6 = soln.exist([["A"]],"A") #true
	test7 = soln.exist([["A","A","A"],["A","A","A"],["A","A","B"]], "AAAAAAAAA") #false

	assert test1 == False
	assert test2 == False
	assert test3 == True
	assert test4 == True
	assert test5 == True
	assert test6 == True
	assert test7 == False










