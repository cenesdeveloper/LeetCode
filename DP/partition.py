class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        Solution 
        1 - state variable is i and cursum
        2 - first check if sum(nums) % 2 == 0
        3 - use top down approach to recursively add numbers and check if we reach target
        4 - recurrence: memo[(i, cursum)] = dp(i+1, cursum) or dp(i+1, cursum + nums[i])
        5 - base cases: if cursum == total return True, if i == len(nums) or cursum > target return False
        6 - memoize the recursion
        """
        if sum(nums) % 2 != 0:
            return False

        target = sum(nums) // 2    
        memo = {}

        def dp(i, cursum):
            if cursum == target:
                return True
            
            if i == len(nums) or cursum > target:
                return False
            
            if (i, cursum) in memo:
                return memo[(i, cursum)]
            
            memo[(i, cursum)] = dp(i+1, cursum) or dp(i+1, cursum + nums[i])
            return memo[(i, cursum)]
        
        return dp(0, 0)