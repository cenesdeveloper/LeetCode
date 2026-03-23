class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Solution
        1 - water is limited by the shortest wall
        2 - water[i] = min(maxLeft, maxRight) - height[i] 
        """

        maxr, maxl = 0, 0
        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            if height[l] < height[r]:
                maxl = max(maxl, height[l])
                res += maxl - height[l]
                l += 1
            else:
                maxr = max(maxr, height[r])
                res += maxr - height[r]
                r -= 1
        return res