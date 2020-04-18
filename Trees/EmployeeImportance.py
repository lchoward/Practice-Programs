# You are given a data structure of employee information, which includes the employee's
# unique id, his importance value and his direct subordinates' id.
#
# For example, employee 1 is the leader of employee 2, and employee 2 is the leader
# of employee 3. They have importance value 15, 10 and 5, respectively. Then employee
# 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10, [3]], and
# employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate of
# employee 1, the relationship is not direct.
#
# Now given the employee information of a company, and an employee id, you need to
# return the total importance value of this employee and all his subordinates.
#
# Example 1:
#
# Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
# Output: 11
# Explanation:
# Employee 1 has importance value 5, and he has two direct subordinates: employee 2
# and employee 3. They both have importance value 3. So the total importance value
# of employee 1 is 5 + 3 + 3 = 11.
#
# Note:
#
# One employee has at most one direct leader and may have several subordinates.
# The maximum number of employees won't exceed 2000.

# approach:
# (1) run bfs from id on the list of subordinates
# (2) if a list is empty return
# (3) add to the importance each time
# (4) return res

# run-time: O(N)
# space: O(N)

# Employee info
from collections import deque

class Employee:
    def __init__(self, id, importance, subordinates):
        """
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        """
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        """
        # helper function that performs dfs
        def bfs(curr_id):
            eid = hashmap[curr_id]
            self.res += self.employees[eid].importance
            for subordinate in self.employees[eid].subordinates:
                stack.append(subordinate)
            return

        # check for empty input
        if not employees:
            return 0
        self.employees = employees
        # put all employees' list index (0 through N-1) in a hashmap
        hashmap = {}
        for i in range(len(self.employees)):
            hashmap[employees[i].id] = i
        
        self.res = 0
        stack = deque()
        stack.append(id)
        while stack:
            curr_employee = stack.pop()
            bfs(curr_employee)
        return self.res

if __name__ == '__main__':
    employee1 = Employee(4,5,[1,-2])
    employee2 = Employee(1,3,[])
    employee3 = Employee(-2,3,[])

    e4 = Employee(1,2,[-10])
    e5 = Employee(-10,3,[])

    elist1 = [employee1, employee2, employee3]
    elist2 = [e4, e5]

    soln = Solution()
    print(soln.getImportance(elist1,4))
    print(soln.getImportance(elist2,1))