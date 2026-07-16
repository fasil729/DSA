class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
      """
        we are asked the number of islands in given grid:
             island is land portion that is surrounded by water in all direc
             the outer part of the grid is water

             1 for land 
             0 for water representation

        what comes to my mind is using traversing the grid through dfs search
           basically i will start with the first cell [0, 0]
           if it is water will break
           if not try to explore every possible land i can acchive thorugh it and mark
           the land visited and when done i count it as the first island

           then continue on each cell this way but will not explored already marked or visted portion


        why this approach work: 
           starting from land it is possible to explore and mark each part of the island
           so we can count every explored land as one island  in one turn
           on the same time since we are trying to check each cell there will be no remaining island

           as a result we can acheive the final correct result
        
      """


      n, m = len(grid), len(grid[0])
      res = 0

      def isValid_index(row, col):
         return 0 <= row < n and 0 <= col < m

      def dfs(row, col):
         if not isValid_index(row, col) or grid[row][col] != "1":
            return
         
         grid[row][col] = "#"
         for r, c in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            n_r, n_c = row + r, col + c
            dfs(n_r, n_c)
         
         

      for row in range(n):
         for col in range(m):
            cell = grid[row][col]
            if cell == "1":
               dfs(row, col)
               res += 1
      
      return res

      
      
   

      

   
      



        
        