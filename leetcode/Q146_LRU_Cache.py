class LRUCache:

    def __init__(self, capacity: int):
        self.stack = []
        self.capacity = capacity
    def get(self, key: int) -> int:
        for i in range(len(self.stack)-1,-1,-1):
            k,v = self.stack[i]
            if k==key:
                self.stack.append(self.stack.pop(i))
                return v
        return -1


    def put(self, key: int, value: int) -> None:
        is_found =False
        for i in range(len(self.stack)):
            k,v = self.stack[i]
            if k==key:
                is_found=True
                self.stack.pop(i)
                self.stack.append((k,value))
                break
        if not is_found:
            if len(self.stack)==self.capacity:
                self.stack.pop(0)
            self.stack.append((key,value))
# Your LRUCache object will be instantiated and called as such:

obj = LRUCache(2)
print(obj.get(2))
obj.put(2, 6)
print(obj.get(1))
obj.put(1, 5)
obj.put(1, 2)
print(obj.get(1))
print(obj.get(2))
