class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        rows, cols = len(matrix), len(matrix[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            best = 1
            for dr, dc in directions:
                nr, nc = dr + i, dc + j
                if 0 <= nr < rows and 0 <= nc < cols:
                    if matrix[nr][nc] > matrix[i][j]:
                        best = max(best, 1 + dp(nr, nc))
            
            memo[(i, j)] = best
            return best 
        
        res = 0
        for r in range(rows):
            for c in range(cols):
                res = max(res, dp(r, c))
        return res

        