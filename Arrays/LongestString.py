# purpose: Given a string, find the length of the longest substring without repeating characters.

from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        strLength = len(s)
        
        # corner case of string size 0
        if (strLength < 1):
            return 0

        # corner case of string size 1
        elif (strLength == 1):
            return 1

        # all other cases
        else:
            currSub = ""
            # maxSubLen = 0
            currSubLen = 0
            # maxSubStr = ""
            # index = 0
            for i in range (0, strLength):
                if (s[i] in currSub):
                    lenRemove = currSub.find(s[i])
                    if (lenRemove == currSubLen - 1):
                        currSub = s[i]
                        currSubLen = 1
                    else:
                        currSub = currSub[lenRemove+1: currSubLen] + s[i]
                        currSubLen = currSubLen - lenRemove
                else:
                    currSub += s[i]
                    currSubLen += 1
                    if (currSubLen > maxSubLen):
                        maxSubLen = currSubLen
                        maxSubStr = currSub
                        index = i
            # print("maxSubStr is: " + maxSubStr + " | index is : " + str(i))
            return maxSubLen

if __name__ == '__main__':
    soln = Solution()
    test1 = soln.lengthOfLongestSubstring("abcabcbb") #should return 3
    test2 = soln.lengthOfLongestSubstring("") #should return 0
    test3 = soln.lengthOfLongestSubstring("0") #should return 1
    test4 = soln.lengthOfLongestSubstring("hhhello") #should return 3
    test5 = soln.lengthOfLongestSubstring("abccharlie") #should return 7
    test6 = soln.lengthOfLongestSubstring("aaa") #should return 1
    test7 = soln.lengthOfLongestSubstring("dvdf") #should return 3
    test8 = soln.lengthOfLongestSubstring("aabaab!bb") #should return 3
    test9 = soln.lengthOfLongestSubstring("aabaabcbb") #should return 3

    assert test1 == 3, "test1 failed"
    assert test2 == 0, "test2 failed"
    assert test3 == 1, "test3 failed"
    assert test4 == 3, "test4 failed"
    assert test5 == 7, "test5 failed"
    assert test6 == 1, "test6 failed"
    assert test7 == 3, "test7 failed"
    assert test8 == 3, "test8 failed"
    assert test9 == 3, "test9 failed"