class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #Create stack and list of operations
        stack = []
        operations = ['+', '-', "*", "/"]
        #Iterate through tokens
        for token in tokens:
            #Check if token is operation, otherwise push to stack
            if token in operations:
                #Add
                if token == "+":
                    num = stack[-2] + stack[-1]
                #Subtract
                elif token == "-":
                    num = stack[-2] - stack[-1]
                #Multiply
                elif token == "*":
                    num = stack[-2] * stack[-1]
                #Division
                else:
                    num = int(stack[-2] / stack[-1])
                #Pop previous entries and add new one
                stack.pop()
                stack.pop()
                stack.append(num)
            else:
                stack.append(int(token))
        return stack[-1]
        