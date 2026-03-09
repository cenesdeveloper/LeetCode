class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Solution
        1 - start from end and for each step check if we can reach to previous (later index)
        2 - move the goal to current index for next iteration
        3 - if we can move the goal to 0 it means last index is reachable
        TC: O(n) MC: O(1)
        """
        goal = len(nums) - 1
        
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0