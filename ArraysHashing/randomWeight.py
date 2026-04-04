class Solution:
    """
    Solution
    1 - create a prefix sum array and calculate prefix sums
    2 - generate a target value in range [1, prefix_sums[-1]]
    3 - do binary search to find which index it would fall into
    """
    def __init__(self, w: List[int]):
        self.prefix_sums = []

        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total = prefix_sum

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)

        l, r = 0, len(self.prefix_sums)-1

        while l < r:
            m = (l + r) // 2
            if target > self.prefix_sums[m]:
                l = m + 1
            else:
                r = m
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()