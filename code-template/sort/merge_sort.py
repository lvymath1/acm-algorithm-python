from typing import List, Tuple


# 递归实现
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

# 非递归实现
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

# [NC349 计算数组的小和](https://www.nowcoder.com/practice/6dca0ebd48f94b4296fc11949e3a91b8)
def calArray(nums: List[int]) -> int:
    n = len(nums)
    width = 1
    ans = 0
    while width < n:
        for i in range(0, n, 2 * width):
            left = nums[i: i + width]
            right = nums[i + width: i + 2 * width]
            res, arr = merge(left, right)
            nums[i: i + 2 * width] = arr
        width *= 2
    return ans

def merge(arr1: List[int], arr2: List[int]):
    i, j = 0, 0
    ans = 0
    arr = []
    tmp = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            arr.append(arr1[i])
            tmp += arr1[i]
            i += 1
        else:
            arr.append(arr2[j])
            ans += tmp
            j += 1
    while i < len(arr1):
        arr.append(arr1[i])
        tmp += arr1[i]
        i += 1
    while j < len(arr2):
        arr.append(arr2[j])
        ans += tmp
        j += 1
    return ans, arr

# [0493. 翻转对](https://leetcode.cn/problems/reverse-pairs/description/)
class Solution:
    def reversePairs(self, nums: List[int]):
        def merge(left: List[int], right: List[int]) -> tuple[list[int], int]:
            result = []
            i = j = res = 0
            while i < len(left) and j < len(right):
                while i < len(left) and left[i] <= 2 * right[j]:
                    i += 1
                else:
                    res += len(left) - i
                    j += 1
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
            return result, res

        n = len(nums)
        ans = 0
        width = 1
        while width < n:
            for i in range(0, n, 2 * width):
                left = nums[i:i + width]
                right = nums[i + width:i + 2 * width]
                arr, res = merge(left, right)
                nums[i:i + 2 * width] = arr
                ans += res
            width *= 2
        return ans