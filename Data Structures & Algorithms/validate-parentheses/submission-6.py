class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash_map = {')' : '(', ']' : '[', '}' : '{'}

        for char in s:
            if (char == '(' or char == '[' or char == '{'):
                stack.append(char)
            else:
                if (len(stack) == 0 or hash_map[char] != stack[-1]):
                    return False
                else:
                    stack.pop()
        if (len(stack) == 0):
            return True
        return False