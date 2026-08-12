class Solution:
    def isValid(self, s: str) -> bool:
        #Create a stack
        stack = []
        #Create hash map of brackets
        brackets = {')' : '(', '}' : '{', ']' : '['}
        #Iterate through string
        for i, c in enumerate (s):
            #Check if character is closing bracket
            if (c == ')' or c == '}' or c == ']'):
                if (len(stack) == 0 or brackets[c] != stack[-1]):
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        #Check if stack is empty
        if (len(stack) != 0):
            return False

        return True