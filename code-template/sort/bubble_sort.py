from typing import List

# 在0~i范围上，相邻较大值数滚下去，最大值来到i，然后在0~i-1的范围上继续
# 时间复杂度: O(n^2)
# 空间复杂度：O(1)
def bubble_sort(arr: List[int]):
    n = len(arr)
    for i in range(n - 1, -1, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [4, 7, 2, 1, 9,6]
print(bubble_sort(arr))
