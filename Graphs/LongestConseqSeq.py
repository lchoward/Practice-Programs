# # Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

# # Your algorithm should run in O(n) complexity.

# Example:

# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.

class Solution:
    # use dfs to search
    def dfs(self, num, visited, hashmap):
        if num in hashmap and visited[hashmap[num]] == False:
            visited[hashmap[num]] = True
            return 1 + self.dfs(num-1, visited, hashmap) + self.dfs(num+1, visited, hashmap)
        return 0
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        visited = [False] * len(nums)
        hashmap = {value:key for key, value in enumerate(nums)}
        max_seq = 0

        for num in nums:
            max_seq = max(max_seq, self.dfs(num, visited, hashmap))

        return max_seq

if __name__ == '__main__':
    soln = Solution()
    test1 = soln.longestConsecutive([]) #0
    test2 = soln.longestConsecutive([100, 4, 200, 1, 3, 2]) #4
    test3 = soln.longestConsecutive([1,3,5,2,4]) #5

    assert test1 == 0
    assert test2 == 4
    assert test3 == 5
