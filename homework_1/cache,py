from collections import OrderedDict


class LRUCache:
    """Least recently used cache class"""
    def __init__(self, capacity: int = 10) -> None:
        self.capacity = capacity
        self.data = OrderedDict()

    def get(self, key: str) -> str:
        if key in self.data:
            value = self.data.pop(key)
            self.data[key] = value
            return value
        return ''

    def set(self, key: str, value: str) -> None:
        if key in self.data:
            self.data.pop(key)

        if len(self.data) >= self.capacity:
            self.data.popitem(last=False)

        self.data[key] = value

    def rem(self, key: str) -> None:
        self.data.pop(key)