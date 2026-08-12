class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for point in points:
            x, y = point
            dist = x**2 + y**2
            heapq.heappush(maxHeap, (-dist, point))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        return [item[1] for item in maxHeap]