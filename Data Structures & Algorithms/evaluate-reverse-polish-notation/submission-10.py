class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #Create stack and set of operations
        stack = []
        operations = {'+', '-', '*', '/'}
        #Traverse list
        for token in tokens:
            if token in operations:
                if token == '+':
                    num = stack[-2] + stack[-1]
                elif token == '-':
                    num = stack[-2] - stack[-1]
                elif token == '*':
                    num = stack[-2] * stack[-1]
                else:
                    num = int(stack[-2] / stack[-1])
                stack.pop()
                stack.pop()
                stack.append(num)
            else:
                stack.append(int(token))
        return stack[-1]
