class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash_map = {'(':')', '{':'}', '[':']'}
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            else:
                if stack:
                    bracket = stack.pop()
                    if c != hash_map[bracket]:
                        return False
                else:
                    return False
        if stack:
            return False
        return True