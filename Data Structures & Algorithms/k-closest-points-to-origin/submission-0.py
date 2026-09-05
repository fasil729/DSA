class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for i, point in enumerate(points):
            dist = (point[0] ** 2 + point[1] ** 2) ** 0.5
            heapq.heappush(max_heap, (-dist, i))

            if len(max_heap) > k:
                heapq.heappop(max_heap)
        

        ans = []
        for _, ind in max_heap:
            ans.append(points[ind])
        
        return ans