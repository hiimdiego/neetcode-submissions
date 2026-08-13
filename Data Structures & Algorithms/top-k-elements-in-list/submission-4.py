class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for i in range(len(nums) + 1)]
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for key, val in freq.items():
            count[val].append(key)
        
        output = []
        for i in range(len(count) - 1, 0, -1):
            for num in count[i]:
                output.append(num)
                if len(output) == k:
                    return output
            
        return output