from sys import stdout


def run():
    left, right = 1, 1000
    while left + 1 < right:
        mid = (left + right) // 2
        print("?", mid, mid)
        x = int(input())
        stdout.flush()
        if mid * mid == x:
            left = mid
        if mid * mid < x:
            right = mid
    print("!", right)

N = int(input())
stdout.flush()
for _ in range(N):
    run()