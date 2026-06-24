class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row
        one_nine = set([str(num) for num in range(1, 10)])
        n, m = len(board), len(board[0])

        for row in range(n):
            digits = one_nine.copy()
            for col in range(m):
                num = board[row][col]
                if num == ".":
                    continue
                if num not in digits:
                    return False

                digits.remove(num)


        # check column
        for col in range(m):
            digits = one_nine.copy()
            for row in range(n):
                num = board[row][col]
                if num == ".":
                    continue

                if num not in digits:
                    return False


                digits.remove(num)

        # check sub-box
        for box in range(9):
            digits = one_nine.copy()
            frow = 3 * (box // 3)
            fcol = 3 * (box % 3)

            for row in range(frow, frow + 3):
                for col in range(fcol, fcol + 3):
                    num = board[row][col]
                    if num == ".":
                        continue

                    if num not in digits:
                        return False

                    digits.remove(num)

        
        return True





        