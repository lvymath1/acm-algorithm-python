def run():
    ls = list(map(int, input().split()))
    ans = 0
    def f(a1, a2, a3, a4):
        win1, win2 = 0, 0
        if a1 > a3:
            win1 += 1
        if a1 < a3:
            win2 += 1
        if a2 > a4:
            win1 += 1
        if a2 < a4:
            win2 += 1
        return 1 if win1 > win2 else 0
    ans += f(ls[0], ls[1], ls[2], ls[3])
    ans += f(ls[1], ls[0], ls[2], ls[3])
    print(ans * 2)

N = int(input())
for _ in range(N):
    run()