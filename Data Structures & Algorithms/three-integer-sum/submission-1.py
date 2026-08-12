class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Create output
        output = []
        #Sort the list
        nums.sort()
        #Iterate through each value of the list
        for i in range(len(nums) - 2):
            #Check if current val is same as previous val
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            #Initialize target and pointers
            target = -nums[i]
            l, r = i + 1, len(nums) - 1
            #while loop
            while l < r:
                #Check if pair is less than target
                if (nums[l] + nums[r] < target):
                    l += 1
                #Check if pair is greater than target
                elif (nums[l] + nums[r] > target):
                    r -= 1
                else:
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return output
                