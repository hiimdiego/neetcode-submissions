class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #only add open parenthesis if open < n
        #only add a closing parenthesis if closed < open
        #valid IIF open == closed == n
        stack = []
        output = []

        def backTrack(openN, closedN):
            if (openN == closedN == n):
                output.append("".join(stack))
                return
            if (openN < n):
                stack.append("(")
                backTrack(openN + 1, closedN)
                stack.pop()
            if (closedN < openN):
                stack.append(")")
                backTrack(openN, closedN + 1)
                stack.pop()
            return
        backTrack(0, 0)
        return output