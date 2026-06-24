class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:

    def __init__(self):
        self.k = 10 ** 3
        self.hash_map = [Node(-1, -1) for _ in range(self.k)]
        

    def put(self, key: int, value: int) -> None: 
        ind = key % self.k
        curr = self.hash_map[ind]

        while curr.next:
            if curr.next.key == key:
                curr.next.value = value
                return
            
            curr = curr.next
        
        curr.next = Node(key, value)
        

    def get(self, key: int) -> int:
        ind = key % self.k
        curr = self.hash_map[ind]

        while curr:
            if curr.key == key:
                return curr.value
        
            curr = curr.next

        return -1


    def remove(self, key: int) -> None:
        ind = key % self.k
        curr = self.hash_map[ind]
        
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            
            curr = curr.next
    
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)