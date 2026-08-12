class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Initialize left and right pointers
        l, r = 0, len(numbers) - 1
        #Traverse list
        for i in range (len(numbers)):
            #Check if sum of pointers > target
            if (numbers[l] + numbers[r] > target):
                r -= 1
            #Check if sum of pointers < target
            elif (numbers[l] + numbers[r] < target):
                l += 1
        #Return set of pointers
        return [l + 1, r + 1]