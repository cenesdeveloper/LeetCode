"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Solution
        1 - Use DFS starting from the given node to traverse the graph
        2 - create clones dicitonary and create nodes and fill it recursively node -> cloned node
        3 - base case: node is already cloned return cloned node
        4 - recursive case: create clone node 
        5 - Recusively clone each nieghbor and append it to the current cloned nodes neighbors
        5 - return clone of the starting node
        """

        if not node:
            return None
        
        clone = {}

        def dfs(n):
            if n in clone:
                return clone[n]
            
            new_node = Node(n.val)
            clone[n] = new_node

            for nei in n.neighbors:
                new_node.neighbors.append(dfs(nei))
            
            return new_node
            
        return dfs(node)