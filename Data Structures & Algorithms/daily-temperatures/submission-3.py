class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Create output and stack
        output = [0] * len (temperatures)
        stack = [] #pair: [idx, temp]

        #Traverse list of temperatures
        for i, temp in enumerate (temperatures):
            #While stack isn't empty and temp > top of stack
            while len(stack) != 0 and temp > stack[-1][1]:
                #Pop stack
                idx, t = stack.pop()
                #Update output
                output[idx] = i - idx
            #Append new value to stack
            stack.append((i, temp))
        return output