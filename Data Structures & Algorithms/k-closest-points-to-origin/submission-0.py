import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for coord in points:
            dist = math.sqrt(coord[0]**2 + coord[1]**2)
            distances.append((-dist, coord))

        heapq.heapify(distances)
        while len(distances) > k:
            heapq.heappop(distances)

        output = [item[1] for item in distances]
        return output
        
        
