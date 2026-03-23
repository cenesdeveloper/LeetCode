class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Solution
        1 - use two pointers one starting from end one from beginnng
        2 - if sum > target do r - 1 else l + 1
        """
        l = 0
        r = len(numbers) - 1

        while l < r:
            tot = numbers[l] + numbers[r]
            if tot > target:
                r -= 1
            elif tot < target:
                l += 1
            else:
                return [l+1, r+1] 