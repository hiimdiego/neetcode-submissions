class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for i in range(len(nums) + 1)]

        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for key, val in freq.items():
            count[val].append(key)
        
        output = []
        for i in range(len(count) - 1, -1, -1):
            vals = count[i]
            for j in range(len(vals)):
                if len(output) != k:
                    output.append(vals[j])
            if len(output) == k:
                break
                
        return output 
            
