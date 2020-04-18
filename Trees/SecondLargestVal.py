# Return the second-largest item in a BST

class Solution:
	def find_largest(node):
		curr_node = node
		if not curr_node:
			return None
		while curr_node:
			if not curr_node.right:
				return curr_node.val
			curr_node = curr_node.right


	def find_second_largest(node):
		curr_node = node
		if not curr_node:
			return None
		while curr_node:
			if not curr_node.right and curr_node.left:
				return find_largest(curr_node.left)
			if not curr_node.right.right and not curr_node.right.left and curr_node.right:
				return curr_node.val
			curr_node = curr_node.right