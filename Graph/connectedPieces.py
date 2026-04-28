class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        Solution
        1 - build an adjacency list
        2 - run dfs on each node starting 0 till n-1
        3 - keep track of seen nodes so we don't run dfs on seen nodes
        4 - count unconnected pieces as each dfs start
        """

        piece = 0
        adj = [[] for _ in range(n)]
        seen = [False] * n
        
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(node):
            if seen[node]:
                return
            
            seen[node] = True
            for nei in adj[node]:
                if not seen[nei]:
                    dfs(nei)
        
        for i in range(n):
            if not seen[i]:
                dfs(i)
                piece += 1
        return piece


        