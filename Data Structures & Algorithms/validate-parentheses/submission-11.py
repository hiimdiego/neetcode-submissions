class Solution:
    def isValid(self, s: str) -> bool:
        #Create stack and hashmap
        stack = []
        brackets = {')':'(', '}':'{', ']':'['}
        #Traverse string
        for c in s:
            if c in brackets:
                if len(stack) == 0 or brackets[c] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        #Check if stack is empty
        if len(stack) != 0:
            return False
        return True