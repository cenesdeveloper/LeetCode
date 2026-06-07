class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            # if pattern is done string needs to be done as well
            if j == len(p):
                return i == len(s)
            
            first = i < len(s) and (s[i] == p[j] or p[j] == '.')

            # Next char is *
            if j + 1 < len(p) and p[j+1] == "*":
                ans = (first and dp(i+1, j)) or dp(i, j+2)
            
            # No *
            else:
                ans = first and dp(i+1, j+1)
            memo[(i, j)] = ans
            return ans
        
        return dp(0, 0)