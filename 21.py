hod = input()
fx = ord(hod[0]) - ord('a') + 1
fy = int(hod[1])
tx = ord(hod[3]) - ord('a') + 1
ty = int(hod[4])
dx = abs(tx - fx)
dy = abs(ty - fy)

if (dx == 1 and dy == 2) or (dx == 2 and dy == 1):
    print("верно")
else:
    print("ошибка")