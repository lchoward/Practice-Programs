# Problem: Given a collection of intervals, merge all overlapping intervals.
# Note: = are considered overlapping
#
# Example 1:
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
#
# Example 2:
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

# approach:
# (1) sort intervals by start index
# (2) start from front and merge as needed

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res

if __name__ == '__main__':
    soln = Solution()
    test1 = soln.merge([]) #[]
    test2 = soln.merge([[1,4],[4,5]]) #[1,5]
    test3 = soln.merge([[1,4],[0,6]]) #[0,6]
    test4 = soln.merge([[1,3],[2,6],[8,10],[10,18]]) #[[1,6],[8,18]]

    assert test1 == []
    assert test2 == [[1,5]]
    assert test3 == [[0,6]]
    assert test4 == [[1,6],[8,18]]