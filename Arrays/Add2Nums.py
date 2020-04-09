# purpose: add two numbers, which are represented backwards as linked nodes

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # calculate l1 first
        val1 = l1.val #l1 value
        string1 = str(val1) #string of l1 values
        nextNode1 = l1.next #l1 next node
        
        # go through each node in l1
        while (nextNode1 != None):
            val1 = nextNode1.val
            nextNode1 = nextNode1.next
            string1 = str(val1) + string1
        
        num1 = int(string1)
        
        # calculate l2 next
        val2 = l2.val #l2 value
        string2 = str(val2) #string of l2 values
        nextNode2 = l2.next #l2 next node
        
        # go through each node in l2
        while (nextNode2 != None):
            val2 = nextNode2.val
            nextNode2 = nextNode2.next
            string2 = str(val2) + string2
        
        num2 = int(string2)
        
        # get the sum as a list of integers
        sum = num1 + num2
        listSum = list(map(int, str(sum)))
        sumLength = len(listSum)
        
        # convert back to a listNode
        if (sumLength == 1):
            output = ListNode(sum)
            return output
        else: 
            for i in range(0,sumLength-1):
                if (i == 0):
                    lastNode = ListNode(listSum[0])
                    prevNode = ListNode(listSum[1])
                    prevNode.next = lastNode
                    currNode = prevNode
                else:
                    currNode = ListNode(listSum[i+1])
                    currNode.next = prevNode
                    prevNode = currNode
            output = currNode
            return output

if __name__ == '__main__':
    # run a test on something easy
    test1 = Solution()
    l1 = ListNode(0)
    l2 = ListNode(0)
    print(test1.addTwoNumbers(l1, l2))

