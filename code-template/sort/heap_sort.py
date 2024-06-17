class MaxHeap:
    def __init__(self, array=None):
        if array is None:
            self.heap = []
        else:
            self.heap = array
            self._build_max_heap()

    def _parent(self, index):
        return (index - 1) // 2

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _heapify_down(self, index):
        left_child_index = self._left_child(index)
        right_child_index = self._right_child(index)
        largest = index

        if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
            largest = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
            largest = right_child_index

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def _build_max_heap(self):
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)

    def insert(self, key):
        self.heap.append(key)
        index = len(self.heap) - 1
        parent_index = self._parent(index)
        while index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = self._parent(index)

    def extract_max(self):
        if len(self.heap) == 0:
            raise IndexError("extract_max from an empty heap")
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def get_max(self):
        if len(self.heap) == 0:
            raise IndexError("get_max from an empty heap")
        return self.heap[0]

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0


def heap_sort(array):
    # Step 1: Build a max heap
    n = len(array)
    max_heap = MaxHeap(array)
    # Step 2: Extract elements from the heap to sort the array
    sorted_array = [0] * n
    i = 0
    while not max_heap.is_empty():
        sorted_array[n - i - 1] = max_heap.extract_max()
        i += 1
    return sorted_array

unsorted_array = [10, 20, 5, 30, 15]
sorted_array = heap_sort(unsorted_array)
print("Sorted array:", sorted_array)