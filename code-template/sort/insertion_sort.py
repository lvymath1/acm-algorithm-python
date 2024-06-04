from typing import List


# 0~i范围上已经有序，新来的数从右向左滑到不再小的位置插入，然后继续
def insertion_sort(arr: List[int]):
    n = len(arr)
    for i in range(n):
        for j in range(i-1, -1, -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                break
    return arr

arr = [4, 7, 2, 1, 9,6]
print(insertion_sort(arr))