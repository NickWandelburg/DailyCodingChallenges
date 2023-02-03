# HeapSort sorting algorithm
import random

class Heap:
    def __init__(self):
        # heap is represented as a list
        self.heap = []

    def add(self, data):
        # add data to the end of the heap
        self.heap.append(data)
        # get index of added data
        index = len(self.heap) - 1
        # get parent index
        parent_index = (index - 1) // 2
        # while data is smaller than parent
        while index > 0 and self.heap[index] < self.heap[parent_index]:
            # swap data and parent
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            # get new index
            index = parent_index
            # get new parent index
            parent_index = (index - 1) // 2

    def extract_min(self):
        # get minimum value
        min_value = self.heap[0]
        # get last value
        last_value = self.heap.pop()
        # if heap is not empty
        if len(self.heap) > 0:
            # set last value as root
            self.heap[0] = last_value
            # get index of root
            index = 0
            # get left child index
            left_child_index = 2 * index + 1
            # get right child index
            right_child_index = 2 * index + 2
            # while left child exists
            while left_child_index < len(self.heap):
                # get smaller child index
                smaller_child_index = left_child_index
                # if right child exists and is smaller than left child
                if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[left_child_index]:
                    # set smaller child index to right child index
                    smaller_child_index = right_child_index
                # if root is smaller than smaller child, break
                if self.heap[index] < self.heap[smaller_child_index]:
                    break
                # swap root and smaller child
                self.heap[index], self.heap[smaller_child_index] = self.heap[smaller_child_index], self.heap[index]
                # get new index
                index = smaller_child_index
                # get new left child index
                left_child_index = 2 * index + 1
                # get new right child index
                right_child_index = 2 * index
        # return minimum value
        return min_value

def heap_sort(data):
    # create heap
    heap = Heap()
    # add data to heap
    for i in data:
        heap.add(i)
    # get sorted data
    sorted_data = []
    # sort data in ascending order
    for i in range(len(data)):
        sorted_data.append(heap.extract_min())
    return sorted_data


if __name__ == '__main__':
    # generate 10 random integers in range 0-100
    data = [random.randint(0, 100) for i in range(10)]

    # sort data with HeapSort
    sorted_data = heap_sort(data)

    print("Unsorted data: ", data)
    print("Sorted data: ", sorted_data)
