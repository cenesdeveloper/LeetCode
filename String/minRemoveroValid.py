class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        Solution
        1 - keep track of openning brackets using stack
        2 - if there is an unmatched openning or closing bracket remove it

        TC: O(n), MC: O(n)
        """

        stack = []
        pos = set()
        res = []

        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack:
                    stack.pop()
                else:
                    pos.add(i)

        # Get all the positons of openning brackets that were not closed
        while stack:
            pos.add(stack.pop())
        
        # Delete all invalid brakcets
        for i in range(len(s)):
            if i not in pos:
                res.append(s[i])
        return "".join(res)
        
            
