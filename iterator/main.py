from abc import ABC, abstractmethod


# Iterator interface
class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self):
        pass


# Concrete Iterator
class ArrayIterator(Iterator):
    def __init__(self, items):
        self._items = items
        self._position = 0

    def has_next(self) -> bool:
        return self._position < len(self._items)

    def next(self):
        if self.has_next():
            item = self._items[self._position]
            self._position += 1
            return item
        raise StopIteration("No more elements")


# Usage
if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    iterator = ArrayIterator(data)

    while iterator.has_next():
        print(iterator.next())
