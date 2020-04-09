# Problem Description: determine if a linked list has a cycle

class Solution:
    def hasCycle(self, head):
    	"""
    	:type head: ListNode
    	:rtype: bool
    	"""
        if head == None:
            return False
        hashmap = {}
        curr_node = head
        count = 0
        while curr_node.next != None:
            if curr_node in hashmap:
                return True
            hashmap[curr_node] = count
            curr_node = curr_node.next
            count += 1
        return False