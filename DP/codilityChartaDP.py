"""
Question:

Given a string s consisting of lowercase English letters, determine the minimum
number of characters that must be removed so that the remaining characters form
a string whose characters are in non-decreasing lexicographical order.

A string is considered sorted if for every index i:

    s[i] <= s[i + 1]

You may remove characters from any positions, but the relative order of the
remaining characters must be preserved.

Return the minimum number of characters that need to be removed.

Note:
The returned value cannot be less than 3.

Example 1:
Input: s = "banana"
Output: 3

Explanation:
Removing three characters can leave "aaa" or "bnn", both of which are sorted.

Example 2:
Input: s = "abcde"
Output: 3

Explanation:
The string is already sorted, requiring 0 removals, but the minimum return
value is 3.

Constraints:
    1 <= len(s) <= 10^4
    s contains only lowercase English letters.
"""

def longestIncreasingSub(s):
    dp = [1] * len(s)
    
    for i in range(len(s)):
        for j in range(i):
            if s[i] >= s[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return len(s) - max(dp)
    
    
    
    
    
    
    