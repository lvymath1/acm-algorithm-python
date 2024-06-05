import bisect
from typing import List


# 找 >= 最左位置, 不存在返回列表长度
def bisect_ge_left(arr, x):
    return bisect.bisect_left(arr, x)

# 找 <= 最右位置，不存在返回-1
def bisect_le_right(arr, x):
    return bisect.bisect_right(arr, x) - 1

"""
二分答案:
[162. 寻找峰值](https://leetcode.cn/problems/find-peak-element/description/)
"""
def findPeakElement(nums: List[int]) -> int:
    n = len(nums)
    left, right = -1, n
    while left + 1 < right:
        mid = (left + right) // 2
        if (mid == 0 or nums[mid - 1] < nums[mid]):
            left = mid
        else:
            right = mid
    return left