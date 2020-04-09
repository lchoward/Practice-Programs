# description:
# Given two strings text1 and text2, return the length of their longest common
# subsequence.

# A subsequence of a string is a new string generated from the original string with some
# characters(can be none) deleted without changing the relative order of the remaining
# characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common 
# subsequence of two strings is a subsequence that is common to both strings.

#If there is no common subsequence, return 0.

from typing import List

class Solution:
	def longestCommonSubsequence(self, text1: str, text2: str) -> int:
		len1 = len(text1)
		len2 = len(text2)

		# corner case: empty string(s)
		if(len1 == 0 or len2 ==0):
			return 0

		# otherwise, use a 2-d array to store answer
		memo = [[0] * (len2+1) for i in range(len1+1)]

		# print(str(memo))

		# scan through both strings and increment if there's a match
		for i in range(1, len1+1):
			for j in range(1, len2+1):
				if(text1[i-1] == text2[j-1]):
					memo[i][j] = 1 + memo[i-1][j-1]
				else:
					memo[i][j] = max(memo[i-1][j],memo[i][j-1])

		return memo[len1][len2]

if __name__ == '__main__':
	soln = Solution()
	test1 = soln.longestCommonSubsequence("","a") # should return 0
	test2 = soln.longestCommonSubsequence("a","b") # should return 0
	test3 = soln.longestCommonSubsequence("0abc","cdef") # should return 1
	test4 = soln.longestCommonSubsequence("0abc","cdef0") # should return 1
	test5 = soln.longestCommonSubsequence("abcde","ace") # should return 3
	test6 = soln.longestCommonSubsequence("aba","aaaaa") # should return 2
	test7 = soln.longestCommonSubsequence("pmjghexybyrgzczy",
		"hafcdqbgncrcbihkd") # should return 4

	assert test1 == 0
	assert test2 == 0
	assert test3 == 1
	assert test4 == 1
	assert test5 == 3
	assert test6 == 2
	assert test7 == 4
