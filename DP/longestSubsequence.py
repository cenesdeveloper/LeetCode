class Solution:
    def lengthOfLIS(self, nums) -> int:
        """
        Solution
        1 - state variable i is the ith element
        2 - dp[i] returns the longest increasing subsequence ending at i
        3 - recurrence relation: dp[i] = max(dp[j] + 1) for all j < i
        4 - base case: all elements are 1 because all are starting of an increasing subarray 
        5 - Final answer is max(dp)
        """

        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)