# Description: You're working with an intern that keeps coming to you with JavaScript code
# that won't run because the braces, brackets, and parentheses are off. To save you both
# some time, you decide to write a braces/brackets/parentheses validator.

# Let's say:
# '(', '{', '[' are called "openers."
# ')', '}', ']' are called "closers."
# We want an efficient function that tells us whether or not an input string's openers and
# closers are properly nested.

# Examples:

# "{ [ ] ( ) }" should return True
# "{ [ ( ] ) }" should return False
# "{ [ }" should return False

class Solution:
	def bracketValid(self, s):
		currBracket = ""
		brackets = []
		counter = 0
		isvalid = True
		needRight = False
		leftBrackets = ('(','{','[')
		rightBrackets = (')','}',']')


		# go through each character in the string
		for char in s:
			if(char in leftBrackets):
				currBracket = char
				brackets.append(char)
				counter += 0
			
			if(char in rightBrackets):
				# check for )
				if(char == ')'):
					if(currBracket == '('):
						brackets.pop()
						counter -= 1
						if(counter>=0):
							currBracket = brackets[counter]
						else:
							currBracket = ''
					else:
						return False
				# check for ]
				elif(char in rightBrackets):
					if(char == ']'):
						if(currBracket == '['):
							brackets.pop()
							counter -= 1
							if(counter>=0):
								currBracket = brackets[counter]
							else:
								currBracket = ''
						else:
							return False
				# check for }
				elif(char in rightBrackets):
					if(char == '}'):
						if(currBracket == '{'):
							brackets.pop()
							counter -= 1
							if(counter>=0):
								currBracket = brackets[counter]
							else:
								currBracket = ''
						else:
							return False

		# after for loop, check if we have unmatched bracket
		if(currBracket != ''):
			return False
		else:
			return True

if __name__ == '__main__':
	soln = Solution()
	test1 = soln.bracketValid("hello world") #True
	test2 = soln.bracketValid("this is[cr]{az}(y)") #True
	test3 = soln.bracketValid("{[(])}") #False
	test4 = soln.bracketValid("hello(") #False

	assert test1 == True
	assert test2 == True
	assert test3 == False
	assert test4 == False