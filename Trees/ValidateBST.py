# Validate that a tree is a binary search tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        
        minimum = float('-inf')
        maximum = float('inf')
        return (self.valid(root.left, minimum, root.val) and
        self.valid(root.right, root.val, maximum))
        
    def valid(self, node, minimum, maximum):
        if node == None: return True
        if minimum >= node.val or node.val >= maximum: return False
        if self.valid(node.left, minimum, node.val) == False: return False
        return self.valid(node.right, node.val, maximum)