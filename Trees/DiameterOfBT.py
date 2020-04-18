# Given a binary tree, you need to compute the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two
# nodes in a tree. This path may or may not pass through the root.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# approach:
# (1) run dfs on left and right children of root
# (2) in dfs, update res to the sum of the left and right depths if needed
# (3) compare res w/ depth of root's left and right children, return max
# runtime: O(N)
# space: O(N)


class Solution:
    def dfs(self, node):
        if not node:
            return 0
        else:
            left = 1 + self.dfs(node.left)
            right = 1 + self.dfs(node.right)
            if left + right - 2 > self.res:
                self.res = left + right - 2
            return max(left, right)

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not node:
            return 0
        self.res = 0

        l = self.dfs(root.left)
        r = self.dfs(root.right)
        return max(self.res, l + r)

if __name__ == '__main__':
    soln = Solution()
    root = TreeNode(1)
    left1 = TreeNode(2)
    left2 = TreeNode(3)
    right1 = TreeNode(10)
    right2 = TreeNode(11)
    root.left = left1
    left1.left = left2
    root.right = right1
    right1.right = right2

    assert soln.diameterOfBinaryTree(root) == 4