class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Solution
        1 - 2 state variables i and j
        2 - dp(i, j) returns min number of operations at i and j
        3 - recurrence -> if same dp(i+1, j+1) else insert dp(i, j+1), delete(i+1,j), replace(i+1, j+1)
        4 - base case if i == len(word1) then return len(word2) - j, if j == len(word2) then return len(word1) - i
        5 - Memoize each stage
        """
        memo = {}

        def dp(i, j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if (i, j) in memo:
                return memo[(i, j)]
            if word1[i] == word2[j]:
                ans = dp(i+1, j+1)

            else:
                ins = dp(i, j+1)
                delete = dp(i+1, j)
                rep = dp(i+1, j+1)
                ans = min(ins, delete, rep) + 1

            memo[(i, j)] = ans
            return ans
        return dp(0, 0)