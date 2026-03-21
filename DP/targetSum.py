class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        Solution
        1 - we have 2 state varaibles position and total
        2 - dp(i, tot) should return total ways to reach total for position i
        3 - for each position we can add or subtract
        4 - base cases: i == len(nums), total > target, total == target
        5 - memoize solution
        """

        memo = {}

        def dp(i, tot):
            if i == len(nums):
                return 0 if tot != target else 1

            if (i, tot) in memo:
                return memo[(i, tot)]
            
            add = dp(i+1, tot + nums[i])
            sub = dp(i+1, tot - nums[i])

            memo[(i, tot)] = add + sub
            return memo[(i, tot)]

        return dp(0, 0)
            