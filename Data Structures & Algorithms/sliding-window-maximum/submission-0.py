class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        start = 0
        
        
         
        # building starting queue
        for i in range(k):
            num = nums[i]
            while queue and queue[-1] < num:
                queue.pop()

            queue.append(num)


        ans = [queue[0]]
        # iterate through possible windows and update queue and build the answer array

        for end in range(k, len(nums)):
            if queue[0] == nums[start]:
                queue.popleft()
            start += 1
            num = nums[end]
            while queue and queue[-1] < num:
                queue.pop()

            queue.append(num)

            ans.append(queue[0])
        
        return ans

        
        