class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #base case
        if len(stones) == 1: return stones[0]
        if len(stones) == 2: return max(stones[0] - stones[1], stones[1] - stones[0])
        #turn list into max_heap
        max_heap = [-n for n in stones]
        heapq.heapify(max_heap)
        #while loop
        while len(max_heap) > 1:
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)
            #test cases
            if x == y:
                continue
            elif x < y:
                y = y - x
                heapq.heappush(max_heap, -y)
            else:
                x = x - y
                heapq.heappush(max_heap, -x)

        #return
        if len(max_heap) == 0:
            return 0
        return -max_heap[0]
