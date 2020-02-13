# process input
str_num = raw_input("What is your number: ")
num = int(str_num)

#quick maths
remainder = num % 2

if (remainder == 0):
	print ("Your number, %s, is even." % str_num)
else:
	print ("Your number, %s, is odd." % str_num)