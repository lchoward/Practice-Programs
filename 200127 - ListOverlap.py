# determines common items in two lists
import random
len1 = random.randint(1,10)
len2 = random.randint(1,10)

list1 = []
list2 = []
overlap = []

for i in range(0,len1):
	randomNum1 = random.randint(1,20)
	list1.append(randomNum1)
for j in range(0,len2):
	randomNum2 = random.randint(1,20)
	list2.append(randomNum2)
for num in list1:
	if (num in list2):
		overlap.append(num)


print("list 1 is: ")
print(list1)
print("list 2 is: ")
print(list2)


if (len(overlap) == 0):
	print("There are no overlapping numbers")
elif (len(overlap) == 1):
	print("The overlapping number is: %s" % str(overlap[0]))
else:
	print("The numbers in list 1 that overlap with those in list 2 are: ")
	print(overlap)