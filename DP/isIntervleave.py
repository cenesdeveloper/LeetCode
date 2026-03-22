class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        Solution
        1 - We have 3 state variables i, j, k pointers to s1, s2, s3
        2 - dp(i, j, k) should return True or False for i, j, k saying on i, j, k we can have interleaving or not
        3 - recurence relation: if (s[i] == s[k] and dp(i+1,j, k+1)) or (s[j] == s[k] and dp(i, j+1, k+1)) True else False
        4 - Base Cases: if i == len(s1) check if s2[j:] == s3[k:], if j == len(s2) check if s1[i:] == s3[k:], check at the beginning if len(s1) + len(s2) == len(s3)
        5 - memoize the solution
        """
        if len(s1) + len(s2) != len(s3):
            return False

        memo = {}

        def dp(i, j, k):
            if i == len(s1):
                return s2[j:] == s3[k:]
            
            if j == len(s2):
                return s1[i:] == s3[k:]
            
            if (i, j, k) in memo:
                return memo[(i, j, k)]

            ans = False
            if (s1[i] == s3[k] and dp(i+1, j, k+1)) or (s2[j] == s3[k] and dp(i, j+1, k+1)):
                ans = True
            memo[(i, j, k)] = ans
            return ans
        return dp(0, 0, 0)
             