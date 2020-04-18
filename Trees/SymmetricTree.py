# Determine if a tree is symmetric

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# approach:
# (1) run bfs, passing depth as an argument
# (2) append values to an array, where arr[i] gives the level order traversal for nodes
#     at depth = i, including null roots (node == None)
# (3) starting w/ depth = 1, check that arr[depth][j] = arr[depth][length - j - 1]
# (4) return True if make it through all checks

from collections import deque
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        if root == None:
            return True
        dq = deque()
        dq.append((root, 0))
        hashmap = {}
        
        def bfs(node, depth):
            if node == None:
                if depth not in hashmap:
                    hashmap[depth] = [None]
                else:
                    hashmap[depth].append(None)
                return
            else:
                if depth not in hashmap:
                    hashmap[depth] = [node.val]
                else:
                    hashmap[depth].append(node.val)
                dq.append((node.left, depth + 1))
                dq.append((node.right, depth + 1))
                return
        
        # add all node values to the hashmap via bfs
        while dq:
            (curr_node, depth) = dq.popleft()
            bfs(curr_node, depth)
        
        # iterate through the hashmap
        i = 1
        while hashmap.get(i):
            curr_len = len(hashmap[i])
            if curr_len % 2 != 0:
                return False
            for j in range(int(curr_len / 2)):
                if hashmap[i][j] != hashmap[i][curr_len - j - 1]:
                    return False
            i += 1
        
        return True