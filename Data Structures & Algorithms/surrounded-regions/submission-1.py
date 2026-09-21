class Solution:
    def solve(self, board: List[List[str]]) -> None:

        ROWS, COLS = len(board), len(board[0])
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()


        def is_valid(row, col):
            return 0 <= row < ROWS and 0 <= col < COLS


        def dfs(row, col):
            if (row, col) in visited or board[row][col] == "X":
                return

            visited.add((row, col))
            for dr, dc in DIRECTIONS:
                nr, nc = row + dr, col + dc
                if is_valid(nr, nc):
                    dfs(nr, nc)

            


        

        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)

        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)

        

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited:
                    board[r][c] = "X"
        

        