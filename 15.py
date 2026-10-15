n, k, m = map(int, input().split())

if k == m:
    print(0)
else:
    frw = abs(m - k)
    bck = n - frw
    print(min(frw, bck) - 1)