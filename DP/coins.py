class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """ 
        Solution
        1 - State variable is i the ith amount
        2 - dp[i] returns min number of coins to make i amount
        3 - recurrence relation: dp[i] = min(dp[i], dp[i - c] + 1)
        4 - base case: all amounts start with float("inf") because we will check for min and amount 0 is 0 coins
        5 - return dp[amount] if dp[amount] != inf else -1
        """

        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i-c] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1