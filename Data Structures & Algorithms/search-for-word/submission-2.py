class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]


]
      word = "CAT"

      nodes that is connected horizntally and vertically  and then we are asked to if there is any
      path that equals the given word

      having every node as starting node and then search for paths

      start with a explore every possible path
        then contue wih b all and if i get valid one i will return true
 
        
        """

        Rows = len(board)
        Cols = len(board[0])
        n = len(word)
        visited = set()

        def isValid(row, col):
          if (row, col) in visited:
            return False
          if 0 <= row < Rows and 0 <= col < Cols:
            return True
          
          return False

        def dfs(row, col, ind):
          if word[ind] != board[row][col]:
            return False

          if ind == n - 1:
            return True
          
          
          
          directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
          visited.add((row, col))
          
          for direc in directions:
            new_row, new_col = row + direc[0], col + direc[1]
            if isValid(new_row, new_col) and dfs(new_row, new_col, ind + 1):
              return True
          
          visited.remove((row, col))
          return False




          

        
        for row in range(Rows):
          for col in range(Cols):
            if dfs(row, col, 0):
              return True
        
        return False






        
        