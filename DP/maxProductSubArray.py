class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Solution
        1 - Keep track of max seen so far and min seen so far because of the negative signs the min seen so far can become and positive and bigger
        2 - In a for loop calculate maxseen = max(maxseen * num, minseen * num, num)
        minseen = min(maxseen * num, minseen * num, num)
        3 - when calculating min use pre calculation of max for that loop
        4 - keep track of max of res and maxseen
        """

        res, maxs, mins = 0, 0, 0

        for i in range(len(nums)):
            temp = maxs

            maxs = max(maxs * nums[i], mins * nums[i], nums[i])
            mins = min(temp * nums[i], mins * nums[i], nums[i])

            res = max(res, maxs)
        return res