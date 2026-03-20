class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        Solution
        1 - create dp array where dp[i][j] = dp[i-1][j] + dp[i][j-1]
        2 - if there is an obstacle than count that cell as 0
        3 - first row and first col is 0 after seeing an obstacle
        """
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * cols for _ in range(rows)]

        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

        for i in range(rows):
            for j in range(cols):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] += dp[i-1][j]
                    if j > 0:
                        dp[i][j] += dp[i][j-1]

        return dp[rows-1][cols-1]