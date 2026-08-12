class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #Combine both arrays into one [position, speed]
        cars = zip(position, speed) 
        #Sort array based on positions in descending order
        cars = sorted(cars, reverse=True)
        #Create stack
        stack = []
        #Traverse list of cars
        for car in cars:
            #Calculate time needed to reach target
            time = (target - car[0])/car[1]
            stack.append(time)
            #Compare times and pop stack if necessary
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
                    