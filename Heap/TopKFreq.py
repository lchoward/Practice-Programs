# Problem Description:
# Given a non-empty array of integers, return the k most frequent elements.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
# Note:

# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the
# array's size.

import math 

class Solution:
    # build the hashmap from the nums array
    def initiate_map(self, nums, hashmap):
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        return

    # try to insert an element into the heap
    def try_insert(self, heap, item, size, k):
        if size < k:
            heap[size] = item
            self.add_to_heap(heap, item, size, k)
            return
        else:
            (curr_min, curr_val) = heap[0]
            (our_freq, our_val) = item
            if our_freq > curr_min:
                heap[0] = item
                self.heapify(heap, 0, k)
            return
    
    # try_insert call this when adding to the heap and current size < k
    def add_to_heap(self, heap, item, i, k):
        if i == 0:
            return

        # otherwise, get parent and see if we need to swap
        p = math.floor((i-1)/2)
        (p_freq, p_val) = heap[p]
        (curr_freq, curr_val) = item

        if curr_freq <= p_freq:
            heap[p] = item
            heap[i] = (p_freq, p_val)
            # perform the same steps recursively as needed on the new parent node
            self.add_to_heap(heap, item, p, k)
        return

    # try_insert calls this method for adding to the heap if it is already at capacity
    def heapify(self, heap, i, k):
        (curr_freq, curr_val) = heap[i]
        l, r = i*2+1, i*2+2

        min_freq = curr_freq
        min_val = curr_val
        min_index = i
        
        # compare with children to find which is the min
        if l < k:
            (l_freq, l_val) = heap[l]
            if l_freq < min_freq:
                min_freq = l_freq
                min_val = l_val
                min_index = l
        if r < k:
            (r_freq, r_val) = heap[r]
            if r_freq < min_freq:
                min_freq = r_freq
                min_val = r_val
                min_index = r

        # if the min is one of the children, then we need to perform a swap
        if min_index != i:
            heap[i] = (min_freq, min_val)
            heap[min_index] = (curr_freq, curr_val)
            # perform heapify recursively as needed
            self.heapify(heap, min_index, k)
        return

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        hashmap = {}
        heap = [None] * k
        size = 0
        output = [0] * k

        self.initiate_map(nums, hashmap)

        for key, value in hashmap.items():
            self.try_insert(heap, (value, key), size, k)
            if(size != k):
                size += 1
            # print("size is: " + str(size))
            # print(heap)

        for i in range(k):
            (curr_freq, curr_val) = heap[i]
            output[i] = curr_val

        return output

if __name__ == '__main__':
    soln = Solution()
    test1 = soln.topKFrequent([1], 1) #[1]
    test2 = soln.topKFrequent([1,1,1,2,2,3], 2) #[1,2]
    test3 = soln.topKFrequent([-1,1], 1) #[-1]
    test4 = soln.topKFrequent([10,10,10,11,11,11,12,12,12,12,5,5,5,5],3) #[10,5,12]

    assert test1 == [1]
    assert test2 == [2,1]
    assert test3 == [-1]
    assert test4 == [10,5,12]