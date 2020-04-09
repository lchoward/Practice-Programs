# Given a collection of intervals, find the minimum number of intervals you need to remove
# to make the rest of the intervals non-overlapping.
# Note: = are not considered overlapping (e.g., [0,1] and [1,2])
#
# Example 1:
# Input: [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
#
# Example 2:
# Input: [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
#
# Example 3:
# Input: [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already
# non-overlapping.

# approach:
# (1) see which intervals overlap
# (2) store overlapping intervals in a List[int], where overlaps[i] gives indices of
#     intervals that overlap with the ith interval
# (3) go through the list, starting with the maximum and remove it from any other lists;
#     repeat until finished
# (4) return the number of intervals removed
class Solution:
	def eraseOverlapIntervals(self, intervals):
		"""
		:type intervals: List[List[int]]
		:rtype: List[List[int]]
		"""
		if intervals == []:
			return 0

		intervals.sort(key = lambda x:x[1]) # sort by end (ascending)
		# print(intervals)
		end = intervals[0][0]
		remove = 0
		for [start_i, end_i] in intervals:
			if start_i < end:
				remove += 1
			else:
				end = end_i

		return remove

if __name__ == '__main__':
	soln = Solution()
	test1 = soln.eraseOverlapIntervals([]) #0
	test2 = soln.eraseOverlapIntervals([[1,2]]) #0
	test3 = soln.eraseOverlapIntervals([[1,2],[2,3]]) #0
	test4 = soln.eraseOverlapIntervals([[1,3],[2,3],[1,2]]) #1
	test5 = soln.eraseOverlapIntervals([[0,2],[1,3],[1,3],[2,4],[3,5],[3,5],[4,6]]) #4
	test6 = soln.eraseOverlapIntervals([[2,3],[1,4],[3,5],[1,9]]) #2

	assert test1 == 0
	assert test2 == 0
	assert test3 == 0
	assert test4 == 1
	assert test5 == 4
	assert test6 == 2
