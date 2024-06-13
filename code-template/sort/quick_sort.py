from random import random
from typing import List


def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr

    pivot_index = int(len(arr) * random())
    pivot = arr[pivot_index]

    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    return quick_sort(less) + equal + quick_sort(greater)


if __name__ == "__main__":
    arr = [4, 7, 2, 1, 9, 6]
    print("原始数组:", arr)
    sorted_arr = quick_sort(arr)
    print("排序后数组:", sorted_arr)
