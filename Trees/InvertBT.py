# Invert a binary tree.

# Example:

# Input:

#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# Output:

#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
# Trivia:
# This problem was inspired by this original tweet by Max Howell:
#
# Google: 90% of our engineers use the software you wrote (Homebrew),
# but you can’t invert a binary tree on a whiteboard so f*** off.

# approach:
# run dfs on root, inverting left and right children of the node each time
# return root
# run-time: O(N)
# space: O(N) if needed O(1) could use a while loop?

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
	def invertTree(self, root):
		"""
		:type root: TreeNode
		:rtype: TreeNode
		"""
		if not root:
			return None
		def dfs(node):
			if not node:
				return

		dfs(root)
		return root
