class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        heapq.heapify(maxHeap)
        for point in points:
            x, y = point
            dist = x*x + y*y
            heapq.heappush(maxHeap, (-dist, point))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        output = [item[1] for item in maxHeap]
        return output