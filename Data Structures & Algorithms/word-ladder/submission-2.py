from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        
        while queue:
            word, distance = queue.popleft()
            
            if word == endWord:
                return distance
            
            # Generate all 1-character variations: O(26 * N)
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c == word[i]:
                        continue
                    
                    next_word = word[:i] + c + word[i+1:]
                    
                    if next_word in word_set and next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, distance + 1))
                        
        return 0