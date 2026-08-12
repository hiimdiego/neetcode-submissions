class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for point in points:
            x, y = point
            dist = x*x + y*y
            heapq.heappush(max_heap, (-dist, point))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        output = [item[1] for item in max_heap]
        return output
        