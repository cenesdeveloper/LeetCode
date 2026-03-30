class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        Solution
        1 - before array is -inf after end is -inf again meaning it will have some peak then it will decrease
        2 - check for nums[m] > nums[m+1] if True the slope is decreasing and peak at left else you are on increasing slope and peak is at right
        3 - Do Binary Search and check nums[m] > nums[m+1] if True r = m else l = m + 1
        """
            
        l, r = 0, len(nums) - 1

        while l < r:
            m = (r + l) // 2

            if nums[m] > nums[m + 1]:
                r = m
            
            else:
                l = m + 1
        return l
            
        