from typing import List


def bubble_sort(arr: List[int]):
    n = len(arr)
    for i in range(n - 1, -1, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [4, 7, 2, 1, 9,6]
print(bubble_sort(arr))
