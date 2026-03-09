class Solution:
    def maxSum(self, nums: List[int]) -> int:
        """
        Solution
        1 - if sum < 0 then reset sum back to 0
        2 - start adding each number
        3 - after each addition compare with max
        """
        if len(nums) == 1:
            return nums[0]

        tot = 0
        maxs = nums[0]
        for i in range(len(nums)):
            if tot < 0:
                tot = 0
            tot += nums[i]
            maxs = max(maxs, tot)
        return maxs