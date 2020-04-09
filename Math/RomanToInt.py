# Conver roman string to integer

class Solution:
    def romanToInt(self, s):
    	"""
    	:type s: str
    	:rtype: int
    	"""
        if not s:
            return 0
        
        # initialize data for quick access
        romans = "IVXLCDM"
        values = [1, 5, 10, 50, 100, 500, 1000]
        length = len(s)
        index = [None] * length
        sum = 0
        
        # set values for index array
        for i in range(length):
            char = s[i]
            index[i] = romans.find(char)
        
        # process the characters from back
        prev_value = values[index[length - 1]]
        sum = prev_value
        for i in reversed(range(length - 1)):
            curr_value = values[index[i]]
            if curr_value < prev_value: sum -= curr_value
            else: sum += curr_value
            prev_value = curr_value
        
        return sum