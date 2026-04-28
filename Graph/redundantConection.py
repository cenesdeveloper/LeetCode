class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        Solution
        1. Build adjacency list incrementally
        2. For each edge (a, b), run DFS to check if b is reachable from a
        3. If reachable → adding this edge creates a cycle → return it
        4. Otherwise, add the edge and continue
        """

        adj = [[] for _ in range(len(edges) + 1)]
        
        def dfs(node, target, seen):
            if node == target:
                return True
            
            seen.add(node)
            for nei in adj[node]:
                if nei not in seen:
                    if dfs(nei, target, seen):
                        return True
            return False

        for a, b in edges:
            seen = set()

            if dfs(a, b, seen):
                return [a, b]

            adj[a].append(b)
            adj[b].append(a)