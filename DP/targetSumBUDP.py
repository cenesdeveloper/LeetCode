class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        tot = sum(nums)

        dp = [[0] * (2 * tot + 1) for _ in range(len(nums))]

        dp[0][nums[0] + tot] = 1
        dp[0][-nums[0] + tot] += 1

        for i in range(1, len(nums)):
            for s in range(-tot, tot + 1):
                if dp[i-1][s + tot] > 0:
                    dp[i][s + tot + nums[i]] += dp[i-1][s + tot] 
                    dp[i][s + tot - nums[i]] += dp[i-1][s + tot]
        return dp[len(nums)-1][target + tot] 
