a, b = map(int, input().split('x'))
r = 6.5
d2 = (a ** 2 + b ** 2) ** 0.5 / 2
if d2 <= r:
    print('да')
else:
    print('нет')