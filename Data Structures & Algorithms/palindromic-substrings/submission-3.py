class Solution:
    def countSubstrings(self, s: str) -> int:
        """
         "ABBA" --> "BB" ""
         "BCB" --> "c"

         to find all substrigs that are palindrome in given substring
         let say we have (i, j)  where i is starting index where j is ending index

         we will try to check if s[i:j] is palindrome using the mechanisim given above by checking the first if s[i] == s[j] and if s[i + 1:j - 1] is palindrome as well and count the number through this will be brute force solution and have o(n^3)
         we can optimize checking for palindrome by using dynamic programming to make sure (i, j) is calcualted once 
                          

    
        """
        n = len(s)
        is_pal = [[False] * n for _ in range(n)]
        


        def dp(i, j):
            if is_pal[i][j] or j - i <= 0:
                return True
            
            
            
            if s[i] == s[j] and dp(i + 1, j - 1):
                is_pal[i][j] = True
            
            return is_pal[i][j]



        
        pal_count = 0
        for i in range(n):
            for j in range(i, n):
                if dp(i, j) == True:
                    pal_count += 1
        
        return pal_count
        