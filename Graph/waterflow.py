class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        def dfs(r, c, seen, prevh):
            if r not in range(rows) or c not in range(cols) or (r, c) in seen or heights[r][c] < prevh:
                return
            
            seen.add((r, c))

            dfs(r+1, c, seen, heights[r][c])
            dfs(r, c+1, seen, heights[r][c])
            dfs(r-1, c, seen, heights[r][c])
            dfs(r, c-1, seen, heights[r][c])
            return
        
        # run dfs on top and bottom rows
        for i in range(cols):
            # top row
            dfs(0, i, pac, heights[0][i])
            # bottom row
            dfs(rows-1, i, atl, heights[rows-1][i])
        
        # run dfs on first and last cols
        for i in range(rows):
            # first column
            dfs(i, 0, pac, heights[i][0])
            # last column
            dfs(i, cols-1, atl, heights[i][cols-1])
        
        # check if grid is in both pacific and atlantic
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res