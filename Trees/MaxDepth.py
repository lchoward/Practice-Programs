# Description:
# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root node down 
# to the farthest leaf node.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        maximum = 0
        if root == None:
            return 0
        
        def dfs(node):
            if node == None:
                return 0
            else:
                left = 1 + dfs(node.left)
                right = 1 + dfs(node.right)
                return max(left, right)
        
        return dfs(root)