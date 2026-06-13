class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = [[False] * (len(s2)+1) for _ in range(len(s1) + 1)]
        dp[0][0] = True

        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i == 0 and j == 0:
                    continue
                
                elif i == 0:
                    dp[i][j] = s2[j-1] == s3[i+j-1] and dp[i][j-1]
                
                elif j == 0:
                    dp[i][j] = s1[i-1] == s3[i+j-1] and dp[i-1][j]
                
                else:
                    dp[i][j] = (s1[i-1] == s3[i+j-1] and dp[i-1][j]) or (s2[j-1] == s3[i+j-1] and dp[i][j-1])
        return dp[len(s1)][len(s2)]