from typing import List

# 在i~n-1范围上，找到最小值放到i位置，然后在i+1~n-1范围上继续
# 时间复杂度: O(n^2)
# 空间复杂度：O(1)
def selection_sort(arr: List[int]):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
        print(arr)
    return arr

arr = [4, 7, 2, 1, 9,6]
print(selection_sort(arr))