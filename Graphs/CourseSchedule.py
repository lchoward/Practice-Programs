# Description:
# There are a total of n courses you have to take, labeled from 0 to n-1.
# Some courses may have prerequisites, for example to take course 0 you have to first take
# course 1, which is expressed as a pair: [0,1]. Given the total number of courses and a
# list of prerequisite pairs, is it possible for you to finish all courses?

# Example 1:
# Input: 2, [[1,0]] 
# Output: true
# Explanation: There are a total of 2 courses to take. To take course 1 you should have
# finished course 0. So it is possible.

# Example 2:
# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you
# should also have finished course 1. So it is impossible.

# Note:
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices.
# Read more about how a graph is represented. You may assume that there are no duplicate
# edges in the input prerequisites.

from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # corner case: 0 courses
        if(numCourses == 0):
            return False

        # takeClass[i] indicates if we can take class i; prereqs[i] contains the pre-
        # requisite courses for class i
        takeClass = [True]*numCourses
        prereqs = []
        numPrereqs = 0
        for i in range(numCourses):
            prereqs.append([])

        # iterate through prerequisites
        for preReqPair in prerequisites:
            if(len(preReqPair) <= 1):
                continue
            else:
                course = preReqPair[0]
                needed = preReqPair[1]
                if(course >= numCourses):
                    continue
                elif(needed >= numCourses):
                    return False
                else:
                    prereqs[course].append(needed)
                    takeClass[course] = False
                    numPrereqs += 1

        # build out graph to determine if we can take class num
        def reqIterator(num, takeClass, count):
            if(count > numCourses):
                return False
            if(takeClass[num] == True):
                return True
            else:
                for prereq in prereqs[num]:
                    if(takeClass[prereq] == True):
                        continue
                    else:
                        check = reqIterator(prereq, takeClass, count+1)
                        if(check):
                            continue
                        else:
                            return False
                takeClass[prereq] = True
                return True

        # call on reqIterator for any classes that have prereqs
        for i in range(numCourses):
            if(takeClass[i] == False):
                check = reqIterator(i,takeClass,0)
                if(not check):
                    return False

        return True

if __name__ == '__main__':
    soln = Solution()
    test1 = soln.canFinish(2,[[1,0]]) #true
    test2 = soln.canFinish(2,[[0,1],[1,0]]) #false
    test3 = soln.canFinish(3,[[2,1],[1,0]]) #true
    test4 = soln.canFinish(3,[[2,1],[1,0],[0,2]]) #false
    test5 = soln.canFinish(1,[[1,0],[2,5]]) #true
    test6 = soln.canFinish(1,[[0,5]]) #false
    test7 = soln.canFinish(4,[[2,0],[1,0],[3,1],[3,2],[1,3]]) #false

    assert test1 == True
    assert test2 == False
    assert test3 == True
    assert test4 == False
    assert test5 == True
    assert test6 == False




