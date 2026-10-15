n, m = map(int, input().split('x'))
k = int(input())

f = 0

if k % m == 0:
    i = k // m
    if 1 <= i <= n - 1:
        f = 1

if k % n == 0:
    j = k // n
    if 1 <= j <= m - 1:
        f = 1

if f == 1:
    print("успешно")
else:
    print("неосуществимо")