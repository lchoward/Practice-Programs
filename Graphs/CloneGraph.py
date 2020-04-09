# Description:
# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.
# Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.
# Constraints:
# 1 <= Node.val <= 100
# Node.val is unique for each node.
# Number of Nodes will not exceed 100.
# There is no repeated edges and no self-loops in the graph.
# The Graph is connected and all nodes can be visited starting from the given node.

from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

# Main Code
class Solution:
	def cloneGraph(self, node: Node) -> Node:

		# dictionary to store created nodes
		currGraph = {}

		# helper function to iterate through nodes and create nodes
		def nodeBuild(node, currGraph):
			# check for empty graph or no neighbors
			if(node == None):
				return None
			# check for 1-node graph
			if(node.neighbors == []):
				return Node(node.val)

			# otherwise, go through neighbors DFS
			newNode = Node(node.val)
			currGraph[node.val] = newNode

			for neighbor in node.neighbors:
				if(neighbor.val not in currGraph):
					newerNode = nodeBuild(neighbor, currGraph)
				newNode.neighbors.append(currGraph[neighbor.val])

			return newNode

		outputGraph = nodeBuild(node, currGraph)
		return outputGraph

