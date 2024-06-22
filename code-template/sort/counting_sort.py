def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # 因为数字是0-9

    # 计算每个数字在当前位出现的次数
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # 计算位置索引
    for i in range(1, 10):
        count[i] += count[i - 1]

    # 构建输出数组
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # 将排序后的结果复制回原数组
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    # 找到最大数字以确定需要的位数
    max1 = max(arr)
    exp = 1
    while max1 // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10

# 测试基数排序
if __name__ == "__main__":
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    print("原始数组:", arr)
    radix_sort(arr)
    print("排序后的数组:", arr)
