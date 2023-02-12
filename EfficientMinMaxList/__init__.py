# List that returns the min and max value in O(1)
import random


class EfficientMinMaxList(list):
    def __init__(self):
        super().__init__()
        self._min = None
        self._max = None

    def append(self, num: int) -> None:
        # If the list is empty, set the min and max to the first appended number
        if len(self) == 0:
            self._min = num
            self._max = num
        else:
            # Check if the number is greater than the max and update it if it is
            self._max = self._max if self._max > num else num
            # Check if the number is less than the min and update it if it is
            self._min = self._min if self._min < num else num
        super(EfficientMinMaxList, self).append(num)

    def min(self) -> int:
        return self._min

    def max(self) -> int:
        return self._max


if __name__ == '__main__':
    # Create an empty EfficientMinMaxList
    data = EfficientMinMaxList()

    # Append 10 random numbers to the list
    for i in range(10):
        data.append(random.randint(0, 100))

    print(f"Data: {data}")
    print(f"Minimum: {data.min()}")
    print(f"Maximum: {data.max()}")

