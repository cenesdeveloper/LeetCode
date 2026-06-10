class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Solution
        1 - state variable is i the position in s
        2 - dp[i] returns True or False if we can construct s[0:i+1] with wordDict
        3 - recurrence relation: dp[i] = True if s[j:i] in WordDict and dp[j]
        4 - Base case: empty string always true
        """

        dp = [False] * len(s)
        
        for i in range(len(s)):
            for word in wordDict:
                if i < len(word) - 1:
                    continue
                
                if i == len(word) - 1 or dp[i - len(word)]:
                    if s[i - len(word) + 1:i+1] == word:
                        dp[i] = True
                        break
        return dp[-1]
