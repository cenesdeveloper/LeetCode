class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Solution
        1 - ans[i] = nums[0:i] * nums[i+1:]
        2 - use variable pre for calculating pre product for each element
        3 - loop each element from start and multiply pre
        3 - use variable post for calculating post product for each element
        4 - start from end and loop backwards to calculate post for each element
        """
        pre = 1
        ans = [0] * len(nums)

        for i in range(len(nums)):
            ans[i] = pre
            pre *= nums[i]
        
        post = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= post
            post *= nums[i]
        return ans
