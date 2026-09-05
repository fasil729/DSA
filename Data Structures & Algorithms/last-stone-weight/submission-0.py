class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for stone in stones:
            max_heap.append(-stone)
        
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            maxi_1, maxi_2 = heapq.heappop(max_heap), heapq.heappop(max_heap)

            heapq.heappush(max_heap, maxi_1 - maxi_2)

        
        return -max_heap[0]
        