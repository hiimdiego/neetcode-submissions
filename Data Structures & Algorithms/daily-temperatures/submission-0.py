class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Create output and stack
        output = [0] * len(temperatures)
        stack = [] #pair: [temp, idx]

        #Traverse list of temperatures
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                output[stackInd] = i - stackInd
            stack.append((t, i))

        return output