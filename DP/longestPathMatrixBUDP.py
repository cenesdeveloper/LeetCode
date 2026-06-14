class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        dp = [[1] * cols for _ in range(rows)]

        cells = []

        for r in range(rows):
            for c in range(cols):
                cells.append((matrix[r][c], r, c))
        
        cells.sort(reverse=True)

        for val, r, c in cells:
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    dp[r][c] = max(dp[r][c], 1+dp[nr][nc])

        return max(max(row) for row in dp)