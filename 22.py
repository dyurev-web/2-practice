n, k, m = map(int, input().split())

pr = 2 * n
ses = (pr + k - 1) // k
print(ses * m)