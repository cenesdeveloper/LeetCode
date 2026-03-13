class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Solution
        1 - create dp array where dp[i][j] represents num of palindrome at i to j
        2 - reccurence relation dp[i][j] = 1 + dp[i+1][j-1]
        """

        dp = [[False] * len(s) for _ in range(len(s))]
        count = 0

        for i in range(len(s)-1,-1,-1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    count += 1
        return count