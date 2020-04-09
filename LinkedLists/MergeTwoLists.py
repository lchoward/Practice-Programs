# Problem description: merge two sorted linked lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        arr1 = []
        arr2 = []
    
        arr1.append(l1.val)
        count1 = 1
        curr_node = l1
        while curr_node.next != None:
            count1 += 1 
            arr1.append(curr_node.next.val)
            curr_node = curr_node.next

        arr2.append(l2.val)
        count2 = 1
        curr_node = l2
        while curr_node.next != None:
            count2 += 1
            arr2.append(curr_node.next.val)
            curr_node = curr_node.next

        i, j = 0, 0
        if arr1[0] <= arr2[0]:
            res = ListNode(arr1[0])
            i += 1
        else:
            res = ListNode(arr2[0])
            j += 1
        curr_node = res
        while i < count1 or j < count2:
            if i == count1:
                next_node = ListNode(arr2[j])
                curr_node.next = next_node
                curr_node = next_node
                j += 1
            elif j == count2:
                next_node = ListNode(arr1[i])
                curr_node.next = next_node
                curr_node = next_node
                i += 1
            elif arr2[j] < arr1[i]:
                next_node = ListNode(arr2[j])
                curr_node.next = next_node
                curr_node = next_node
                j += 1
            else:
                next_node = ListNode(arr1[i])
                curr_node.next = next_node
                curr_node = next_node
                i += 1

        return res
