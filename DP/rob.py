class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Solution
        1 - State variable is i
        2 - dp[i] should return max money at ith index
        3 - recurrence: dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        4 - base case: dp[0] = nums[0], dp[1] = max(nums[0], nums[1])
        """
        if len(nums) <= 2:
            return max(nums)
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[len(nums)-1]