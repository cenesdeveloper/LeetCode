class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        
        Solution
        1 - Use set to make O(1) lookups without sorting
        2 - check if we have +1 of our current number in set if so start counting and count till next element not in it
        """
        longest = 0
        numset = set(nums)

        for num in numset:
           
            if num-1 not in numset:
                i = 1
                while num + i in numset:
                    i += 1
                longest = max(longest, i)
        return longest