# Purpose: Given an unsorted array A of size N of non-negative integers, 
# find a continuous sub-array which adds to a given number S.

import random
import sys

def findSubArray(fullArray, sum):
	size = len(fullArray)
	runningSum = 0

	# input checks / error handling
	if (size == 0):
		raise Exception("The array is empty.")
	for i in fullArray:
		if (i < 0):
			raise Exception("The array cannot have negative integers. %i is at fault" % i)
		if (type(i) is not int):
			raise Exception("The array must be only integers. %i is at fault" % i)
	if (type(sum) is not int):
		raise Exception("The desired sum S must be an integer. %i is at fault" % i)

	# inputs look good, let's proceed!
	for i in range(0,size):
		# case 1: the ith item is equal to the sum
		if (fullArray[i] == sum):
			return [fullArray[i]]
		# case 2: ith item < sum so we scan the next item(s)
		elif (i < sum):
			runningSum = fullArray[i]
			for j in range (i+1,size):
				if (runningSum + fullArray[j] == sum):
					return fullArray[i:j+1]
				elif (runningSum + fullArray[j] < sum):
					runningSum += fullArray[j]
		# case 3: ith item > sum, move to the next


# execute some pre-built tests, a random test, and the tests in the input file
if __name__ == "__main__":
	print("Test 1: " + str(findSubArray([1,2,3,4,5,6,7,8,9,10], 4)))
	# to test if it picks up the first sub-array [2, 3] rather than [5]
	print("Test 2: " + str(findSubArray([1,2,3,4,5,6,7,8,9,10], 5)))
	# to test where there is no solution
	print("Test 3: " + str(findSubArray([1,2,3,4,5,6,7,8,9,10], 0)))
	# to test random values
	ranLength = random.randint(1,10)
	ranSum = random.randint(0,20)
	ranArray = []
	for i in range(0,ranLength):
		ranArray.append(random.randint(1,10))
	print("ranArray is: " + str(ranArray) + " || ranSum is: " + str(ranSum))
	print("Test 4: " + str(findSubArray(ranArray,ranSum)))

	# execute tests from input file
	try:
		testFile = sys.argv[1]
		tests = open(testFile,'r')
		numTests = int(tests.readline()[0])
		for i in range (0, numTests):
			firstLine = list(tests.readline().split(" "))
			secondLine = list(tests.readline().split(" "))
			lenArray = int(firstLine[0])
			desiredSum = int(firstLine[1])
			strTestArray = secondLine[0:lenArray]
			testArray = []
			for item in strTestArray:
				testArray.append(int(item))
			print("Input file test: " + str(findSubArray(testArray,desiredSum)))
		tests.close()
	except:
		print("There is no input or the input file is not properly formatted")
	finally:
		print("Testing done")