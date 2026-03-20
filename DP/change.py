class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        Solution
        1 - use recurison with memo to discover all paths
        2 - for each coin we have 2 options take or skip
        3 - after taking we are looking for amount - coin[i] after skipping we look for same amount
        4 - dp(i, total) = number of ways to reach target starting from index i with current sum total
        5 - base case: if total > amount return 0, if total == amount return 1, if i == len(coins) 
        return 0
        6 - recursive case: dp(i, total) = dp(i+1, total) + dp(i, total + coins[i])
        """

        memo = {}

        def dp(i, tot):
            if tot > amount:
                return 0
            
            if tot == amount:
                return 1
            
            if i == len(coins):
                return 0
            
            if (i, tot) in memo:
                return memo[(i, tot)]
            
            memo[(i, tot)] = dp(i+1, tot) + dp(i, tot + coins[i])
            return memo[(i, tot)] 
        return dp(0, 0)

