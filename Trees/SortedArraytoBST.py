# # Given an array where elements are sorted in ascending order, convert it to a height
# balanced BST.
# For this problem, a height-balanced binary tree is defined as a binary tree in which the
# depth of the two subtrees of every node never differ by more than 1.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from math import floor

# Approach:
# (1) corner case: empty array
# (2) middle value is the root
# (3) iteratively, middle left and middle right are the children of the current node, 
#     given the boundary indices
# (4) call this constructor recursively, starting with the middle value
class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        length = len(nums)
        if length == 0:
            return None
        
        # even = length % 2 == 0
        mid = math.floor(length / 2)
        l_max, r_min = mid - 1, mid + 1
        l_min, r_max = 0, length - 1
        root = TreeNode(mid)

        def insertChild(parent, left, right):
        	if left > right:
        		return None
        	length = right - left
        	mid = math.floor(length / 2)
        	l_max, r_min = mid - 1, mid + 1
        	new_node = TreeNode(nums[mid])
        	new_node.left = insertChild(new_node, left, l_max)
        	new_node.right = insertChild(new_node, r_min, right)
        	return new_node

        root.left = insertChild(root, l_min, l_max)
        root.right = insertChild(root, r_min, r_max)

        return root
