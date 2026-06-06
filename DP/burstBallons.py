class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        memo = {}

        def dp(l, r):
            # empty array
            if l > r:
                return 0
            
            # return if hashed
            if (l, r) in memo:
                return memo[(l, r)]
            
            res = 0
            for i in range(l, r + 1):
                coins = nums[l-1] * nums[i] * nums[r+1]
                coins += dp(l, i-1) + dp(i+1, r)
                res = max(res, coins)
            memo[(l, r)] = res
            return memo[(l, r)]
            
        return dp(1, len(nums)-2)