cl = input()
stolb = ord(cl[0]) - ord('a') + 1
stroka = int(cl[1])

if stolb % 2 == stroka % 2:
    print("чёрный")
else:
    print("белый")