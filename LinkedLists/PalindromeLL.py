# Description: Given a singly linked list, determine if it is a palindrome.

class Solution:
    def isPalindrome(self, head):
    	"""
    	:type head: ListNode
    	:rtype: bool
    	"""
        if head == None:
            return True

        def revLL(head):
        	if head == None:
                return None
            prev_node, curr_node = None, head
            while curr_node != None:
                temp = curr_node.next
                curr_node.next = prev_node
                prev_node = curr_node
                curr_node = temp
            return prev_node

        slow, fast = head, head
        numSwaps = 0 # use this to see how many comparisons to make (e.g., 1 for [5,2,5])
        while fast!= None and fast.next != None:
        	slow = slow.next
        	fast = fast.next.next
        	numSwaps += 1

        # reverse the list from slow and compare numSwaps times starting w/ head
        tail = revLL(slow)
        front = head
        for i in range(numSwaps):
        	if front.val != tail.val:
        		return False
        	front = front.next
        	tail = tail.next

        return True