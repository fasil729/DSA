class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix[0]), len(matrix)
        l, r = 0, (n * m) - 1

        def get_index(mid):
            row = mid // m
            col = mid % m
            return row, col



        while l <= r:
            mid = l + (r - l) // 2
            row, col = get_index(mid)

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid - 1
        

        return False
        