class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        # 1. Quick Pruning: check if board has enough characters
        from collections import Counter
        board_counts = Counter(char for row in board for char in row)
        word_counts = Counter(word)
        for char, count in word_counts.items():
            if board_counts[char] < count:
                return False

        def dfs(r, c, index):
            # Base case: Found the whole word
            if index == len(word):
                return True
            
            # Boundary and mismatch checks
            if (r < 0 or r >= rows or c < 0 or c >= cols or 
                board[r][c] != word[index]):
                return False

            # 2. In-place "Visited" mark
            temp = board[r][c]
            board[r][c] = "#" 

            # Explore 4 directions
            # Using simple addition is faster than a loop for 4 directions
            found = (dfs(r + 1, c, index + 1) or 
                     dfs(r - 1, c, index + 1) or 
                     dfs(r, c + 1, index + 1) or 
                     dfs(r, c - 1, index + 1))

            # 3. Backtrack: restore the character
            board[r][c] = temp
            return found

        # Start DFS only if the first letter matches
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
                        
        return False