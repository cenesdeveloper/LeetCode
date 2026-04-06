class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        Solution
        1 - Trees cannot have loops we need to have n-1 edges because the root node does not have an from parent

        """
        if len(edges) != n-1:
            return False

        adjacent = defaultdict(list)
        for a, b in edges:
            adjacent[a].append(b)
            adjacent[b].append(a)
        
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)
            for nei in adjacent[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        
        if not dfs(0, -1):
            return False
        
        return len(visited) == n
            
        
        