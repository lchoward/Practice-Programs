# purpose: merge two sorted lists of ints
# e.g., [1,2,4,10] and [3,4,5,8] -> [1,2,3,4,4,5,8,10]

from typing import List

class Solution:
	def mergeSortedLists(self, list1: List[int], list2: List[int]) -> List[int]:
		len1 = len(list1)
		len2 = len(list2)
		index1 = 0 # pointer for index in list1
		index2 = 0 # pointer for index in list2
		sortedList = []

		# corner cases
		if(len1 == 0):
			return list2
		elif(len2 == 0):
			return list1

		while(index1 < len1 and index2 < len2):
			if(list1[index1] <= list2[index2]):
				sortedList.append(list1[index1])
				index1 += 1
			else:
				sortedList.append(list2[index2])
				index2 +=1

		# check if more numbers to be added
		if(index1 < len1):
			for i in range(index1, len1):
				sortedList.append(list1[i])

		if(index2 < len2):
			for i in range(index2, len2):
				sortedList.append(list2[i])

		return sortedList

if __name__ == '__main__':
	soln = Solution()
	test1 = soln.mergeSortedLists([],[]) # should be []
	test2 = soln.mergeSortedLists([],[2]) # should be [2]
	test3 = soln.mergeSortedLists([3],[]) # should be [3]
	test4 = soln.mergeSortedLists([1,3,5],[2,4,6]) # should be [1,2,3,4,5,6]
	test5 = soln.mergeSortedLists([1],[10,11]) # should be [1,10,11]
	test6 = soln.mergeSortedLists([20,21],[1,2,3]) # should be [1,2,3,20,21]

	assert test1 == []
	assert test2 == [2]
	assert test3 == [3]
	assert test4 == [1,2,3,4,5,6]
	assert test5 == [1,10,11]
	assert test6 == [1,2,3,20,21]