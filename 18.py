a, b = map(int, input().split('x'))
c, d, e = map(int, input().split('x'))

o1, o2 = min(a, b), max(a, b)
small, big = min(c, d, e), max(c, d, e)
mid = c + d + e - small - big

if mid <= o2 and small <= o1:
    print("да")
else:
    print("нет")