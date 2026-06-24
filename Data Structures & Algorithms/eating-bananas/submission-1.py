class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 0, max(piles)

        def is_possible(k):
            if k == 0:
                return False
            hours = h
            for pile in piles:
                hours -= math.ceil(pile / k)
            
            return hours >= 0


        
        while l < r:
            mid = l + (r - l) // 2
            if is_possible(mid):
                r = mid
            else:
                l = mid + 1
        
        return l
        