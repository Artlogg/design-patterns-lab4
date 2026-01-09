from abc import ABC, abstractmethod

class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass


class BubbleSortStrategy(SortingStrategy):
    def sort(self, data):
        print("Sorting using Bubble Sort")
        return sorted(data)


class QuickSortStrategy(SortingStrategy):
    def sort(self, data):
        print("Sorting using Quick Sort")
        return sorted(data)


class Sorter:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def sort_array(self, data):
        return self._strategy.sort(data)


if __name__ == "__main__":
    data = [5, 3, 8, 4, 2]

    sorter = Sorter(BubbleSortStrategy())
    print(sorter.sort_array(data))

    sorter.set_strategy(QuickSortStrategy())
    print(sorter.sort_array(data))
