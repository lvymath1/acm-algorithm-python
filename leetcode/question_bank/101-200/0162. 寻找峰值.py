from typing import List


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