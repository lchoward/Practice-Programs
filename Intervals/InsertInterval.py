# Given a set of non-overlapping intervals, insert a new interval into the intervals
# (merge if necessary). You may assume that the intervals were initially sorted
# according to their start times.
# Note: = is considered overlapping (e.g., [1,2] overlaps w/ [2,3])
#
# Example 1:
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
#
# Example 2:
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

# approach:
# (1) binary search for starting point, where newInterval[0] <= other interval[1]
# (2) merge interval as needed moving from left to right
# (3) condition for merge is if other interval[0] <= newInterval[1]
class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        # handling empty lists as inputs
        if not intervals and not newInterval:
            return []
        if not intervals:
            return [newInterval]
        if not newInterval:
            return intervals

        # helper function to determine if two intervals overlap
        def overlap(a, b):
            return a[0] <= b[1] and b[0] <= a[1]

        # helper function to find first point of overlap (binary search)
        def search(curr_min, newInterval, l, r):
            if l > r:
                return curr_min
            mid = int((l + r) / 2)
            if overlap(intervals[mid], newInterval):
                return search(mid, newInterval, l, mid - 1)
            left = search(curr_min, newInterval, l, mid - 1)
            if left < curr_min:
                return left
            elif curr_min > r:
                return search(curr_min, newInterval, mid + 1, r)
            else:
                return search(curr_min, newInterval, mid + 1, curr_min - 1)

        numIntervals = len(intervals)
        start = search(numIntervals, newInterval, 0, numIntervals - 1)

        # if no overlap, return original list w/ new interval appended
        res = []
        inserted = False
        if start == numIntervals:
            for i in range(numIntervals):
                if inserted:
                    res.append(intervals[i])
                elif intervals[i][0] > newInterval[0]:
                    res.append(newInterval)
                    res.append(intervals[i])
                    inserted = True
                else:
                    res.append(intervals[i])
            if not inserted:
                res.append(newInterval)
            return res

        # otherwise, add until we hit start
        for i in range(start + 1):
            res.append(intervals[i])

        # once at start, merge as needed
        i = start
        while i < numIntervals and overlap(intervals[i], newInterval):
            res[-1][0] = min(res[-1][0], intervals[i][0], newInterval[0])
            res[-1][1] = max(res[-1][1], intervals[i][1], newInterval[1])
            i += 1
        # now append all after merge
        for j in range(i, numIntervals):
            res.append(intervals[j])

        return res

if __name__ == '__main__':
    soln = Solution()
    test1 = soln.insert([],[1,2]) #[[1,2]]
    test2 = soln.insert([[1,2]],[]) #[[1,2]]
    test3 = soln.insert([],[]) #[]
    test4 = soln.insert([[1,2],[3,5],[6,8]],[2,3]) #[[1,5],[6,8]]
    test5 = soln.insert([[1,2],[6,9]],[2,5]) #[[1,5],[6,9]]
    test6 = soln.insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]) #[[1,2],[3,10],[12,16]]
    test7 = soln.insert([[1,5]],[2,3]) #[[1,5]]
    test8 = soln.insert([[1,5]],[6,8]) #[[1,5],[6,8]]
    test9 = soln.insert([[1,5]],[0,0]) #[[0,0],[1,5]]
    test10 = soln.insert([[1,5],[10,11],[15,2147483647]],[5,7]) #[[1,7],[10,11],[15,2147483647]]
    test11 = soln.insert([[-2147483647,0],[1,5],[10,12]],[5,7]) #[[-2147483647,0][1,7][10,12]]
    assert test1 == [[1,2]]
    assert test2 == [[1,2]]
    assert test3 == []
    assert test4 == [[1,5],[6,8]]
    assert test5 == [[1,5],[6,9]]
    assert test6 == [[1,2],[3,10],[12,16]]
    assert test7 == [[1,5]]
    assert test8 == [[1,5],[6,8]]
    assert test9 == [[0,0],[1,5]]
    assert test10 == [[1,7],[10,11],[15,2147483647]]
    assert test11 == [[-2147483647,0],[1,7],[10,12]]


