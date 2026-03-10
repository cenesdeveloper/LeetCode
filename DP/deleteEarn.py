class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """
        Solution
        1 - calculate points gained by deleting values in a hashmap
        2 - Reccurence relation is dp[i] = max(dp[i+1], dp[i+2] + points[i])
        """
        points = defaultdict(int)
        maxnum = max(nums)

        for num in nums:
            points[num] += num
        
        memo = {}

        def dp(i):
            if i > maxnum:
                return 0
            if i in memo:
                return memo[i]
            
            memo[i] = max(points[i] + dp(i+2), dp(i+1))
            return memo[i]
        
        return dp(0)