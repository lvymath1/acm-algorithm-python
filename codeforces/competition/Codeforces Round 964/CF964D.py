def run():
    s = list(input())
    t = input()
    idx = 0
    n = len(t)
    for i, c in enumerate(s):
        if idx < n and c == t[idx]:
            idx += 1
        if c == "?" and idx < n:
            s[i] = t[idx]
            idx += 1
        elif c == "?" and idx == n:
            s[i] = "a"
    if idx == n:
        print("YES")
        print("".join(s))
    else:
        print("NO")


N = int(input())
for _ in range(N):
    run()