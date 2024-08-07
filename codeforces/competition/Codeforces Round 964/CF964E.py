
def run():
    l, r = list(map(int, input().split()))
    def f(x):
        p = 0
        while x > 0:
            x //= 3
            p += 1
        return p

    def g(l, r):
        ans = 0
        p = 1
        cnt = 1
        # [p, 3p - 1] [l, r]
        while p <= 2 * 10 ** 5:
            ans += max(min(3 * p - 1, r) - max(l, p) + 1, 0) * cnt
            p *= 3
            cnt += 1
        return ans

    ans = 2 * f(l) + g(l+1, r)
    print(ans)

N = int(input())
for _ in range(N):
    run()