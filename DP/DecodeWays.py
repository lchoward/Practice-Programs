# Description:
# A message containing letters from A-Z is being encoded to numbers using the following
# mapping:

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given a non-empty string containing only digits, determine the total number of ways
# to decode it.

# Example 1:
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
#
# Example 2:
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

class Solution:
    def numDecodings(self, s: str) -> int:
        # check for empty string
        lenS = len(s)
        if(lenS <= 1):
            if(s=="0"):
                return 0
            else:
                return lenS

        # check for a bad input related to 0s (e.g., 30,40,50,60,70,80,90,00)
        if(s[0] == "0"):
            return 0
        for i in range(0,lenS-1):
            currInt = int(s[i:i+2])
            if(currInt%10==0 and currInt>29):
                return 0
            elif(currInt==0):
                return 0
        # initialize an array for the string's number of decodings
        decodings = [0] * lenS
        decodings[lenS-1] = 1
        # set up the last two numbers first b/c there are some case specifics
        lastTwoNums = int(s[-2:])
        prevOption1 = False # use to see if prior number is between 1 and 9
        prevOption2 = False # use to see if prior number is between 1 and 6
        # 10 and 20 only have 1 option
        if(lastTwoNums == 10 or lastTwoNums == 20):
            decodings[lenS-2] = 1
            decodings[lenS-1] = 0
        # everything else between 10 and 26 has two options
        if(lastTwoNums>10 and lastTwoNums<27 and lastTwoNums!=20):
            decodings[lenS-2] = 2
        # all other 2-digit numbers can only be made 1 way
        else:
            decodings[lenS-2] = 1

        # process the string from the back to front
        for i in reversed(range(lenS-2)):
            prevInt = int(s[i+1])
            currInt = int(s[i])
            if(currInt==1):
                if(prevInt!=0):
                    decodings[i] = decodings[i+1] + decodings[i+2]
                else:
                    decodings[i] = decodings[i+1]
            elif(currInt==2):
                if(prevInt>0 and prevInt<7):
                    decodings[i] = decodings[i+1] + decodings[i+2]
                else:
                    decodings[i] = decodings[i+1]
            else:
                decodings[i] = decodings[i+1]

        return decodings[0]

if __name__ == '__main__':
    soln = Solution()
    test1 = soln.numDecodings("") #0
    test2 = soln.numDecodings("1") #1
    test3 = soln.numDecodings("11") #2
    test4 = soln.numDecodings("99") #1
    test5 = soln.numDecodings("212") #3
    test6 = soln.numDecodings("2626") #4
    test7 = soln.numDecodings("2121") #5
    test8 = soln.numDecodings("21212") #8
    test9 = soln.numDecodings("222222") #13
    test10 = soln.numDecodings("0") #0
    test11 = soln.numDecodings("00") #0
    test12 = soln.numDecodings("902626") #0
    test13 = soln.numDecodings("2020") #1
    test14 = soln.numDecodings("11020") #2
    test15 = soln.numDecodings("01") #0
    test16 = soln.numDecodings("001") #0
    test17 = soln.numDecodings("99999") #1
    test18 = soln.numDecodings("227") #2
    test19 = soln.numDecodings("19963") #2
    test20 = soln.numDecodings("27999") #1
    test21 = soln.numDecodings("26999") #2
    test22 = soln.numDecodings("11999") #3
    test23 = soln.numDecodings("262") #2

    assert test1 == 0
    assert test2 == 1
    assert test3 == 2
    assert test4 == 1
    assert test5 == 3
    assert test6 == 4
    assert test7 == 5
    assert test8 == 8
    assert test9 == 13
    assert test10 == 0
    assert test11 == 0
    assert test12 == 0
    assert test13 == 1
    assert test14 == 2
    assert test15 == 0
    assert test16 == 0
    assert test17 == 1
    assert test18 == 2
    assert test19 == 2
    assert test20 == 1
    assert test21 == 2
    assert test22 == 3
    assert test23 == 2
                

