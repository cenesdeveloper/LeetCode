class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Solution
        1 - State variables are i, j where they represent slice positon of s
        2 - dp[i][j] returns if s[i:j] is palindrome
        3 - keep track of length with a variable
        4 - Recurrence relation: if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]) dp[i][j] True
        5 - Base case: single length is always True
        """

        dp = [[False] * len(s) for _ in range(len(s))]
        longest = 0
        index = 0

        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True

                    if (j - i + 1) > longest:
                        longest = (j - i + 1)
                        index = i
        return s[index:index+longest]
