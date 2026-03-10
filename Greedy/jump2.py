class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Example
        [2,3,1,1,4] -> 2 -> 3 -> 4

        Solution
        1. Track the farthest index reachable within the current jump range.
        2. When we reach the end of the current range, we must make a jump.
        3. The new range becomes the farthest index we have seen so far.
        """
        farthest = 0
        end = 0
        jump = 0

        for i in range(len(nums)-1):
            if i + nums[i] > farthest:
                farthest = i + nums[i]
            
            if i == end:
                jump += 1
                end = farthest
        return jump
                    
