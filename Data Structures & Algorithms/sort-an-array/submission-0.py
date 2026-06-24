class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr, l, r):
            mid = (l + r) // 2
            left, right = arr[l:mid+1], arr[mid+1:r+1]
            left_ind, right_ind = 0, 0

            while l <= r and left_ind < len(left) and right_ind < len(right):
                if left[left_ind] <= right[right_ind]:
                    arr[l] = left[left_ind]
                    left_ind += 1
                else:
                    arr[l] = right[right_ind]
                    right_ind += 1
                
                l += 1
            
            while l <= r and left_ind < len(left):
                arr[l] = left[left_ind]
                l += 1
                left_ind += 1

            
            while l <= r and right_ind < len(right):
                arr[l] = right[right_ind]
                l += 1
                right_ind += 1



        def mergeSort(arr, l, r):
            if l >= r:
                return
            
            mid = (l + r) // 2
            mergeSort(arr, l, mid)
            mergeSort(arr, mid + 1, r)
            merge(arr, l, r)
        
        mergeSort(nums, 0, len(nums) - 1)
        return nums