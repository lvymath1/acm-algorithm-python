from typing import List

def merge_sort1(arr: List[int]) -> List[int]:
    # 基本情况：如果数组长度小于等于1，则返回数组
    if len(arr) <= 1:
        return arr

    # 将数组分成两半
    mid = len(arr) // 2
    left_half = merge_sort1(arr[:mid])
    right_half = merge_sort1(arr[mid:])

    # 合并两个已排序的子数组
    return merge(left_half, right_half)

def merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    i = j = 0

    # 合并两个子数组
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 添加剩余的元素
    result.extend(left[i:])
    result.extend(right[j:])

    return result

def merge_sort2(arr: List[int]) -> List[int]:
    n = len(arr)
    width = 1
    while width < n:
        for i in range(0, n, 2 * width):
            left = arr[i:i + width]
            right = arr[i + width:i + 2 * width]
            arr[i:i + 2 * width] = merge(left, right)
        width *= 2
    return arr


# 示例用法
if __name__ == "__main__":
    arr = [4, 7, 2, 1, 9, 6]
    arr1 = arr.copy()
    print("原始数组:", arr)
    sorted_arr = merge_sort1(arr)
    print("排序后数组1:", sorted_arr)
    sorted_arr = merge_sort2(arr)
    print("排序后数组2:", sorted_arr)
