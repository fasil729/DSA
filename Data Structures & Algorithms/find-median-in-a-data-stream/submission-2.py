

"""
we asked for median finder class
to add number 
to find median

we should consider better time and space complexity we can acchiev

intiution:
we should add the numbers to the store we have in sorted way since it will help
to find median easly

when finding median we will return the mid number when odd and return the average of mid and mid + 1
when the length is even

for addNum --> we have already sorted list and then we add new num  it will take o(n)

for eg  num =  1 2 3 5 6   and then num = 4   --> O(n)

better approach : 
let have two heaps (one max and one min)
max heap will contain the half number on the left of sorted array
min heap will contain the half numbers on the right of sorted arry

when adding new number there should be careful steps

we will check where the given num should go left or rigth by comparing with top of left and lowest of the right

it can be in left, right or in the mid

if left and mid we will add to the left and then we will check if length of left equals right
   if not equal: we will pop the top and add to the rigth

if right we will add to rigth heap and the check the equality:
    and add the lowest to the left

reason:
when finding median we want two number the top of the left and lowest of the right

find median: 
returns top from the left when odd legnth
top + lowest from the rigth when even lengeth

"""
from heapq import heappop, heappush

from heapq import heappush, heappop

class MedianFinder:
    def __init__(self):
        # max_heap stores the smaller half (negated for Python's min-heap)
        self.small = [] 
        # min_heap stores the larger half
        self.large = [] 

    def addNum(self, num: int) -> None:
        # 1. Always push to the small (max) heap first
        heappush(self.small, -num)
        
        # 2. Make sure every num in small is <= every num in large
        # Pop the largest from small and move it to large
        val = -heappop(self.small)
        heappush(self.large, val)
        
        # 3. Maintain size balance: small can have at most 1 more element than large
        if len(self.large) > len(self.small):
            val = heappop(self.large)
            heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        # If even, return the average of both tops
        return (-self.small[0] + self.large[0]) / 2.0
        




        
        