"""
we are asked to find collection of sets from given nums that sums up to target
we can select same number unlimited times ( 0 ---> infinity)
but the nums we have is positive so it can be ( 0 -- > c  where c = num // target)
intution:
i am kind of thinking to look at all possible condion or combination we can get using backtrioking

we select each number separately and then on second we will add each numbers again to the first set

the base case will be when the sum is passed the target becuase the given numbers is positive.
  
TC --> O(n ** depth)  --- depth = target / min(nums) since it worst case
SC --> recursion stack O(depth)  then ans o(n ** (depth)) since we have n power of depth at max
    the res will be 0(depth) max so final SC --> O(n ** dpth)

"""

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        res = []
        
        # Sort nums to allow for early "break" (optional but helps performance)
        nums.sort() 

        def backtrack(start_index, current_sum):
            if current_sum == target:
                ans.append(res[:]) # Use res[:] or res.copy()
                return
            
            for i in range(start_index, len(nums)):
                # Optimization: If adding this num exceeds target, 
                # because nums is sorted, all numbers after this will also exceed it.
                if current_sum + nums[i] > target:
                    break
                
                res.append(nums[i])
                # We pass 'i' as the next start_index because 
                # we can reuse the same number unlimited times.
                backtrack(i, current_sum + nums[i])
                res.pop() # Backtrack step

        backtrack(0, 0)
        return ans




    
    
        