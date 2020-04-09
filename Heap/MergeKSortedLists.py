# Problem Description:
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its
# complexity.

# Example:

# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6

# Approach: 
# (1) use a priority queue
# (2) insert all linked list vals to the pq
# (3) remember first val --> "firstNode"
# (4) iterate through pq, currNode.val = pq.pop(); prevNode.next = currNode;
#     prevNode = currNode
# (5) return firstNode

from queue import PriorityQueue

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	def mergeKLists(self, lists):
		"""
		:type lists: List[ListNode]
		:rtype: ListNode
		"""
		if len(lists) == 0 and not lists:
			return None

		# get all list node vals into pq
		pq = PriorityQueue()
		counter = 0
		for i in range(len(lists)):
			if lists[i] == None:
				continue
			counter += 1
			curr_node = lists[i]
			curr_val = curr_node.val
			pq.put(curr_val)
			next_node = curr_node.next

			while(next_node != None):
				curr_val = next_node.val
				pq.put(curr_val)
				curr_node = next_node
				next_node = next_node.next

		if counter == 0:
			return None

		# remember the first value
		first_val = pq.get()
		first_node = ListNode(first_val)
		prev_node = first_node
		# go through pq and pop everything
		while not pq.empty():
			curr_val = pq.get()
			curr_node = ListNode(curr_val)
			prev_node.next = curr_node
			prev_node = curr_node
		return first_node

if __name__ == '__main__':
	soln = Solution()
	item1, item2, item3, item4 = ListNode(1), ListNode(2), ListNode(3), ListNode(4)
	test1 = soln.mergeKLists([]) #[]
	test2 = soln.mergeKLists([item1]) #[1]
	test3 = soln.mergeKLists([item4, item3, item2, item1]) #[1,2,3,4]

	print(test1)
	print(test2)
	print(test3)


