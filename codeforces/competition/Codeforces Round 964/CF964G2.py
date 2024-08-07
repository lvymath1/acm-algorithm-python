from sys import stdout


def run():
    left, right = 1, 1000
    while left + 2 < right:
        mid1, mid2 = (left * 2 + right) // 3, (left + right * 2) // 3
        print("?", mid1, mid2)
        x = int(input())
        stdout.flush()
        if x == mid1 * mid2:
            left = mid2
        elif x == mid1 * (mid2 + 1):
            left, right = mid1, mid2
        else:
            right = mid1
    if left + 2 == right:
        print("?", 1, left + 1)
        x = int(input())
        stdout.flush()
        if left + 1 < x:
            right = left + 1
    print("!", right)

N = int(input())
stdout.flush()
for _ in range(N):
    run()