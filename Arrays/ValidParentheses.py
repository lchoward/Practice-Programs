# Determine if brackets are correctly used / ordered

class Solution:
    def isValid(self, s):
    	"""
    	:type s: str
    	:rtype: bool
    	"""
        arr = []
        left, right = "{([", "})]"
        for char in s:
            if char in left:
                arr.append(char)
            elif char in right:
                if not arr:
                    return False
                index = right.find(char)
                if arr.pop() != left[index]:
                    return False
        
        return arr == []