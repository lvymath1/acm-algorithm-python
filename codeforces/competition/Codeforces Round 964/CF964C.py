def run():
    n, s, m = list(map(int, input().split()))
    ans = last = 0
    for i in range(n):
        a, b = list(map(int, input().split()))
        ans = max(ans, a - last)
        last = b
    ans = max(ans, m - last)
    if ans >= s:
        print("YES")
    else:
        print("NO")

N = int(input())
for _ in range(N):
    run()