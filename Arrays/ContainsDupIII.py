# purpose: Given an array of integers, find out whether there are two distinct indices 
# i and j in the array such that the absolute difference between nums[i] and nums[j] is 
# at most t and the absolute difference between i and j is at most k.

from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
    	arrLen = len(nums)

    	# a few corner cases
    	if (arrLen < 2 or k < 1):
    		return False
    	else:
    		numsDict = {}
    		for i in range(0, arrLen):
    			numsDict[i] = nums[i] # dictionary to hold key-values w/ index-num

    		# flip the numsDict to have key-values be nums and lists of indices
    		indexDict = {}
    		for key, value in numsDict.items():
    			if value not in indexDict:
    				indexDict[value] = [key]
    			else:
    				indexDict[value].append(key)

    		nums.sort() #sorted from lowest to highest
    		# print(indexDict)

    		if (arrLen == 2):
    			if (nums[1] - nums[0] <= t):
    				return True

    		# this block of code scans pairs of #s and checks their index difference
    		# if their difference is w/in the threshold
    		for i in range(0,arrLen-1):
    			for j in range(i+1,arrLen):
	    			if (abs(nums[j] - nums[i]) <= t):
	    				indexlist1 = indexDict.get(nums[j])
	    				indexlist2 = indexDict.get(nums[i])
	 
	    				for index1 in indexlist1:  
	    					# print("index 1: " + str(index1))  					
	    					for index2 in indexlist2:
	    						# print("index 2: " + str(index2))
	    						if (abs(index1 - index2) <= k and index1 != index2):
	    							return True
	    			else:
	    				break
    		return False

if __name__ == "__main__":
	soln = Solution()
	test1 = soln.containsNearbyAlmostDuplicate([0,],2,2) # should be False
	test2 = soln.containsNearbyAlmostDuplicate([0,1,-2],3,2) # should be True
	test3 = soln.containsNearbyAlmostDuplicate([1,5,9,1,5,9],2,3) # should be False
	test4 = soln.containsNearbyAlmostDuplicate([1,0,1,1],1,2) # should be True
	test5 = soln.containsNearbyAlmostDuplicate([-1,-1],1,0) # should be True
	test6 = soln.containsNearbyAlmostDuplicate([-3,3],2,4) # should be False
	test7 = soln.containsNearbyAlmostDuplicate([1,2,1],1,1) # should be True

	assert test1 == False, "Test1 failed"
	assert test2 == True, "Test2 failed"
	assert test3 == False, "Test3 failed"
	assert test4 == True, "Test4 failed"
	assert test5 == True, "Test5 failed"
	assert test6 == False, "Test6 failed"
	assert test7 == True, "Test5 failed"

