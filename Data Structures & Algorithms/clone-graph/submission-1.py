"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        visited = set()
        node_map = {}

        def dfs(node):
            if not node:
                return None

            visited.add(node.val)
            n_node = Node(node.val)
            node_map[node.val] = n_node
            n_neighbors = []

            for neigh in node.neighbors:
                if neigh.val in visited:
                    n_neigh = node_map[neigh.val]
                else:
                    n_neigh = dfs(neigh)
                    
                n_neighbors.append(n_neigh)
            
            n_node.neighbors = n_neighbors

            return n_node
        
        return dfs(node)
        