class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # 1. Initialize graph and indegree for EVERY unique letter
        graph = {c: set() for word in words for c in word}
        indegree = {c: 0 for c in graph}

        # 2. Build the graph
        for i in range(len(words) - 1):
            curr_word = words[i]
            next_word = words[i + 1]
            
            # Prefix check (Example 3)
            if len(curr_word) > len(next_word) and curr_word.startswith(next_word):
                return ""
                
            # Find the first different character to create an edge
            for j in range(min(len(curr_word), len(next_word))):
                if curr_word[j] != next_word[j]:
                    u, v = curr_word[j], next_word[j]
                    if v not in graph[u]:
                        graph[u].add(v)
                        indegree[v] += 1
                    break # Only the first difference matters

        # 3. Topological Sort (Kahn's Algorithm)
        queue = deque([node for node in indegree if indegree[node] == 0])
        order = []

        while queue:
            node = queue.popleft()
            order.append(node)

            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # 4. Cycle Detection: Did we process every unique letter?
        if len(order) != len(indegree):
            return ""

        return "".join(order)








# class Solution:
#     def foreignDictionary(self, words: List[str]) -> str:
#         graph = {}
#         indegree = {}

#         # fill the graph
#         for word in words:
#             for letter in word:
#                 graph[letter] = []
#                 indegree[letter] = 0

#         # build directed graph
#         for i in range(len(words) - 1):
#             curr = words[i]
#             nex = words[i + 1]
#             i1, n = 0, len(curr)
#             i2, m = 0, len(nex)

#             while i1 < n and i2 < m and curr[i1] == nex[i2]:
#                 i1 += 1
#                 i2 += 1
            
#             if i1 < n and i2 < m:
#                 graph[curr[i1]].append(nex[i2])
#                 indegree[nex[i2]] += 1
        
#         if len(indegree) == 1:
#             return "".join(indegree.keys())
#         if all(value == 0 for value in indegree.values()):
#            return ""
            
#         # topoligical sort
#         queue = deque([letter for letter in graph if indegree[letter] == 0 ])
#         visited = set()
#         order = ""

#         while queue:
            
#             letter = queue.popleft()
#             if letter in visited: # cycle detected
#                 return ""
#             visited.add(letter) 
#             order += letter

#             for neigh in graph[letter]:
#                 indegree[neigh] -= 1

#                 if indegree[neigh] == 0:
#                     queue.append(neigh)
            

        
#         return order



            





        