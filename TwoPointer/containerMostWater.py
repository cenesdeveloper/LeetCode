class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Solution
        1 - two pointers one starts at start position other starts at end position
        2 - move the smaller one forward or backward
        """

        maxa = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = (r - l) * min(height[l], height[r])

            if height[l] < height[r]:
                l += 1
            
            else:
                r -= 1

            maxa = max(maxa, area)
        return maxa