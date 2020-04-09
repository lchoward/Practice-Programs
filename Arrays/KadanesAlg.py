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

	# corner case
	if (length == 1):
		return inputArray
	else:
		# input array okay, let's go!
		startIndex = 0
		endIndex = 0
		potentialIndex = 0
		startNum = maxSum = runningSum = potentialSum = inputArray[0]

		for i in range(1, length):
			currNum = inputArray[i]
			# case 1: our start number is negative and we see a greater value
			if (startNum < 0 and currNum > startNum):
				startIndex = endIndex = potentialIndex = i
				startNum = maxSum = runningSum = potentialSum = currNum
				
			# case 2: our start number is negative and we see a lower value
			elif(startNum < 0 and currNum <= startNum):
				runningSum += currNum
				
			# case 3: our start number is non-negative, potential sum is less than 
			# the max sum, the potential index is our start, and we see a positive value
			elif(startNum >= 0 and potentialSum < maxSum and potentialIndex == startIndex
			and currNum > 0):
				runningSum += currNum
				
				if (runningSum > maxSum):
					maxSum = runningSum
					endIndex = i
					potentialSum = maxSum
					potentialIndex = i
				if (currNum > maxSum):
					startNum = maxSum = runningSum = potentialSum = currNum
					startIndex = endIndex = potentialIndex = i
			# case 4: our start number is non-negative, we encounter a non-positive value
			elif(startNum >= 0 and currNum <= 0):
				runningSum += currNum
				potentialSum += currNum
				
			## case 5: our start number is non-negative, our running sum is negative
			## and we see a value greater than our max sum
			#elif(startNum >= 0 and runningSum < 0 and currNum > maxSum):
				#startIndex = endIndex = potentialIndex = i
				#startNum = maxSum = runningSum = potentialSum = currNum
				#print("%i is in case 5" % inputArray[i])
				
			# case 5: our start number is non-negative, our running sum is less than the
			# max sum, and we see a value less than our max sum
			elif(startNum >= 0 and runningSum < maxSum and currNum <= maxSum):
				if (potentialIndex == startIndex):
					potentialIndex = i
					potentialSum = currNum
					endIndex = i
					maxSum += currNum
					runningSum += currNum
				elif (potentialSum < 0):
					potentialIndex = i
					potentialSum = currNum
				else:
					potentialSum += currNum
					runningSum += currNum
					if (potentialSum > maxSum and potentialSum > runningSum):
						startIndex = potentialIndex
						endIndex = i
						startNum = inputArray[potentialIndex]
						maxSum = potentialSum
						runningSum = potentialSum
					elif (runningSum > maxSum):
						endIndex = i
						maxSum += currNum

			# case 6: we add the number
			else: 
				endIndex = i
				runningSum += currNum
				maxSum = potentialSum = runningSum
		return inputArray[startIndex:endIndex+1]
				


if __name__ == "__main__":
	# running tests
	# test 1: only one number
	print("test1: " + str(maximizeSum([-1])) + str(maximizeSum([4])))
	# test 2: negative numbers
	print("test2: " + str(maximizeSum([-10,-8,-1,-5,-4])))
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

