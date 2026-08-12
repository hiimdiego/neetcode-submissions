class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Create output
        output = []
        #Sort the list
        nums.sort()
        #Iterate through each value of the list
        for i in range(len(nums) - 2):
            #Check if current val is same as previous 
            if i != 0 and nums[i - 1] == nums[i]:
                continue
            #Initialize target and pointers
            target = -nums[i]
            l, r = i + 1, len(nums) - 1
            #while loop
            while l < r:
                #Check if pair is less than target
                if nums[l] + nums[r] < target:
                    l += 1
                #Check if pair is greater than target
                elif nums[l] + nums[r] > target:
                    r -= 1
                #Otherwise append triplet to list
                else:
                    output.append([nums[l], nums[r], nums[i]])
                    l += 1
                    #Increment left pointer up until it isn't same as previous value
                    while nums[l - 1] == nums[l] and l < r:
                        l += 1
        return output
        
        