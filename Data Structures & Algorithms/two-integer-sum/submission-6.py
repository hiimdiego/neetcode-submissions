class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Create a map of differences to their indices
        hash_map = {}
        #Iterate through list of nums
        for idx, num in enumerate (nums): 
            #Check if num is key in hash_map
            if num in hash_map:
                return [hash_map[num], idx]
            #Otherwise map the difference to the index 
            diff = target - num   
            hash_map[diff] = idx
        return []
