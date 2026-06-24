class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(A) > len(B):
            A, B = B, A
        
        l, r = 0, len(A) - 1

        while True:
            mid = l + (r - l) // 2
            i = half - mid - 2

            Aleft = A[mid] if mid >= 0 else float("-infinity")
            Aright = A[mid + 1] if mid + 1 < len(A) else float("infinity")
            Bleft = B[i] if i >= 0 else float("-infinity")
            Bright = B[i + 1] if i + 1 < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                # Odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = mid - 1
            else:
                l = mid + 1


        



        