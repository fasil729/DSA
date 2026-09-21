from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        """
        beginWord = "cat", 
        endWord = "sag", 
        wordList = ["bat","bag","sag","dag","dot"]

        visited = {  cat, bat, bag,       }
        queue = [   , (dag, 4)    ]
         
         Given leng(wordList) ==> M  leng(beginword) ==> N
        TC: N * M
        SC: N * M
        
        """

        if beginWord == endWord and beginWord not in wordList:
            return 0
        
        queue = deque([(beginWord, 1)])
        visited = set([beginWord])

        def compare_words(word_1, word_2):
            diff = 0

            for ind in range(len(word_1)):
                diff += word_1[ind] != word_2[ind]
            
            return diff == 1
        

        while queue:
            word, distance = queue.popleft()  # word = sag  distance = 4
            

            if word == endWord:
                return distance
            
            for new_word in wordList:  # ["bat","bag","sag","dag","dot"]
                if new_word not in visited and compare_words(word, new_word):
                    queue.append((new_word, distance + 1))
                    visited.add(new_word)
        
        return 0

            



            

        