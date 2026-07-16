"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        d={}
        if node is None:
            return None
        def dfs(old_node):
            if old_node in d:
                return d[old_node]
            clone=Node(old_node.val)
            d[old_node]=clone
            for neigh in old_node.neighbors:
                clone.neighbors.append(dfs(neigh))
            return clone
        return dfs(node)