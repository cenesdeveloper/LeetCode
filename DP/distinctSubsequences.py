class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        Solution
        1 - dp(i, j) returns the number of distinct ways to form t[j:] using chars from s[i:]
        2 - base cases: i == len(s) return 0, j == len(t) return 1
        3 - recurrence relation: dp(i+1, j) always, dp(i+1, j+1) when there is a match
        """
        memo = {}
        
        def dp(i, j):
            if j == len(t):
                return 1
            
            if i == len(s):
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            res = dp(i+1, j)

            if s[i] == t[j]:
                res += dp(i+1, j+1)
            memo[(i, j)] = res
            return res
              
        return dp(0, 0)
            

