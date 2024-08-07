MOD = 10 ** 9 + 7
factor = [0] * (2 * 10 ** 5 + 1)
factor[0] = 1
for i in range(1, 2 * 10 ** 5 + 1):
    factor[i] = (factor[i - 1] * i) % MOD


def comb_mod(n, k, mod=MOD):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    # 计算分子
    numerator = factor[n]
    # 计算分母
    denominator = (factor[k] * factor[n - k]) % MOD
    # 计算逆元
    inverse_denominator = pow(denominator, mod - 2, mod)
    return (numerator * inverse_denominator) % mod


def run():
    n, k = list(map(int, input().split()))
    ls = list(map(int, input().split()))
    cnt = sum(x == 1 for x in ls)
    ans = 0
    for i in range(k // 2 + 1, min(cnt, k) + 1):
        ans = (ans + comb_mod(cnt, i) * comb_mod(n - cnt, k - i)) % MOD
    print(ans)


N = int(input())
for _ in range(N):
    run()
