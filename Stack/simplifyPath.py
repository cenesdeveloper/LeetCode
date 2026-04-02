class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Solution
        1 - Put each element inside stack and whenever you see ../ you pop the last directory from stack
        2 - whenever you see ./ just get rid of it
        3 - at the end construct string using elements inside stack putting '/' between each element
        """

        stack = []

        for dire in path.split("/"):
            if dire == "..":
                if stack:
                    stack.pop()
            elif dire == "." or dire == "":
                continue
            else:
                stack.append(dire)

        res = "/" + "/".join(stack)
        return res

