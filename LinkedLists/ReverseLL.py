# Description:
# Reverse a singly linked list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None

        prev_node, curr_node = None, head

        while curr_node != None:
            temp = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = temp

        return prev_node


if __name__ == '__main__':
    soln = Solution()
    test1 = soln.reverseList(None) # None

    ln1 = ListNode(1)
    ln2 = ListNode(2)
    ln3 = ListNode(3)
    ln4 = ListNode(4)
    ln1.next = ln2
    ln2.next = ln3
    ln3.next = ln4

    test2 = soln.reverseList(ln1)

    print(test1)
    print(test2)