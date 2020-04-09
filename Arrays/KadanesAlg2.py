# Purpose: Given an array arr of N integers. Find the contiguous sub-array with maximum sum.
import sys

def maximizeSum(inputArray):
	# check for bad inputs
	length = len(inputArray)
	if (length == 0):
		raise Exception("The array cannot be empty")
	for i in inputArray:
		if (type(i) is not int):
			raise Exception("The array must be only integers. '" + str(i) + 
				"' is not an integer.")

	# input array okay, let's go!
	sumArray = []
	sumArray.append(inputArray[0])
	currSum = maxSum = inputArray[0]
	for i in range(1, length):
		currNum = inputArray[i]
		if (currSum < 0):
			sumArray.append(currNum)
			currSum = currNum
			if (currSum > maxSum):
				maxSum = currSum
		else:
			currSum += currNum
			sumArray.append(currSum)
			if (currSum > maxSum):
				maxSum = currSum
	return maxSum

			

if __name__ == "__main__":
	# running tests
	# test 1: only one number
	print("test1: " + str(maximizeSum([-1])) + " | " + str(maximizeSum([4])))
	# test 2: negative numbers
	print("test2: " + str(maximizeSum([-10,-8,-3,-5,-4])))
	# test 3: bunch of 0's
	print("test3: " + str(maximizeSum([0,0,0,0,0,0])))
	# test 3: up and down sequence
	print("test4: " + str(maximizeSum([1,-2,0,3,2,4,-1,-2,10,-20,-20,1,2,3,-1,12,-100])))
	# test 4: another up and down sequence
	print("test5: " + str(maximizeSum([1,2,3,4,-3,-7,-1,11,12,-24,40])))

	#run tests from input file (optional)
	try:
		testFile = open(sys.argv[1], 'r')
		line0 = list(testFile.readline().split(" "))
		numTests = int(line0[0])
		for i in range (0, numTests):
			lenArray = int(list(testFile.readline().split(" "))[0])
			secondLine = list(testFile.readline().split(" "))
			testArray = []
			for j in range(0, lenArray):
				testArray.append(int(secondLine[j]))
			print("file test # " + str(i+1) + ": " + str(maximizeSum(testArray)) + " || test array is: " + str(testArray))
		testFile.close()
	except:
		print("Either there is no input file given or it is not formatted correctly")
	finally:
		print("Testing is done.")

