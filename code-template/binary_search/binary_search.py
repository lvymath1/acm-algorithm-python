import bisect


# 找 >= 最左位置, 不存在返回列表长度
def bisect_ge_left(arr, x):
    return bisect.bisect_left(arr, x)

# 找 <= 最右位置，不存在返回-1
def bisect_le_right(arr, x):
    return bisect.bisect_right(arr, x) - 1