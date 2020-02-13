# generate a strong pw for the user

import string
import random

possibleChars = list(string.printable)
numChars = len(possibleChars)

pwLen = int(raw_input("How long do you want your password to be? "))
pwStr = ""

for x in range(0, pwLen):
	randInt = random.randint(0, numChars)
	randChar = possibleChars[randInt]
	pwStr = pwStr + randChar

print("Your password is: %s" %pwStr)