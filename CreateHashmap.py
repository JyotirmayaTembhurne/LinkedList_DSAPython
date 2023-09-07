class MyHashMap:
    def __init__(self):
        self.hashmap = dict()

    def put(self, key: int, value: int) -> None:
        self.hashmap[key] = value

    def get(self, key: int) -> int:
        if key in self.hashmap:
            return self.hashmap[key]
        return -1

    def remove(self, key: int) -> None:
        if key in self.hashmap:
            self.hashmap.pop(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


class MyHashMap:
    def __init__(self):
        self.hashmap = dict()

    def put(self, key: int, value: int) -> None:
        self.hashmap[key] = value

    def get(self, key: int) -> int:
        try:
            return self.hashmap[key]
        except Exception:
            return -1

    def remove(self, key: int) -> None:
        try:
            self.hashmap.pop(key)
        except Exception:
            pass


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
