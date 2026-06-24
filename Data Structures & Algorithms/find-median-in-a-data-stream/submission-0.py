

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

class MedianFinder:

    def __init__(self):
        self.n = 0
        self.left_heap = []
        self.right_heap = []
        

    def addNum(self, num: int) -> None:
        right = float("infinity")
        if self.right_heap:
            right = self.right_heap[0]
        
        # add num
        if num > right:
            heappush(self.right_heap, num)
        else:
            heappush(self.left_heap, - num)
        
        # equalizing
        if len(self.left_heap) - 1 > len(self.right_heap):
            left = - heappop(self.left_heap)
            heappush(self.right_heap, left)
        elif len(self.right_heap) > len(self.left_heap):
            right = - heappop(self.right_heap)
            heappush(self.left_heap, right)
        
        self.n += 1

        return

        

    def findMedian(self) -> float:
        if self.n % 2:
            return - self.left_heap[0]
        
        left = - self.left_heap[0]
        right = self.right_heap[0]
        
        return (left + right) / 2
        




        
        