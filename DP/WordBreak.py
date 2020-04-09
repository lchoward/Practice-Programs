# Description: 
# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
#
# Note:
# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.
#
# Example 1:

# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:

# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
#              Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false

from typing import List

class Solution:
	def wordBreak(self, s: str, wordDict: List[str]) -> bool:
		numWords = len(wordDict)
		strLen = len(s)

		# corner case
		if(s == "" or numWords == 0):
			return 0

		# remove duplicates
		updatedDict = []
		for word in wordDict:
			if word not in updatedDict:
				updatedDict.append(word)

		numWords = len(updatedDict)

		# matched[i] is true if we have a match up to index i
		matched = [False] * (strLen+1)
		matched[0] = True

		# main body: wordBreak(s,wordDict) = wordBreak(s.substring,wordDict)
		for i in range(strLen):
			for j in range(i+1,strLen+1):
				if(s[i:j] in updatedDict and matched[i]):
					matched[j] = True

		return matched[strLen]

if __name__ == '__main__':
	soln = Solution()
	test1 = soln.wordBreak("leetcode", ["leet","yeet","code"]) # true
	test2 = soln.wordBreak("applepenapple",["apple","pen"]) # true
	test3 = soln.wordBreak("catsandog",["cats","dog","sand","and","cat"]) # false
	test4 = soln.wordBreak("",["no"]) # false
	test5 = soln.wordBreak("no",[]) # false
	test6 = soln.wordBreak("catsandog",["cats","dog","and","an"]) # true
	test7 = soln.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])

	assert test1 == True
	assert test2 == True
	assert test3 == False
	assert test4 == False
	assert test5 == False
	assert test6 == True


