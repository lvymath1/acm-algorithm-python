# https://leetcode.cn/problems/two-sum/
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    dic = dict()
    for i, x in enumerate(nums):
        if target - x in dic:
            return [dic[target - x], i]
        dic[x] = i
    return []