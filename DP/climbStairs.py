class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Solution
        1 - state variable is n
        2 - dp(n) should return distinct ways to reach n
        3 - recurrence relation: dp[i] = dp[i-1] + dp[i-2]
        4 - base case: dp[0] = 1, dp[1] = 1
        """

        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]