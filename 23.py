pos = int(input())

if pos == 1:
    print(0)
else:
    pos -= 1

    if pos <= 9:
        print(pos)
    else:
        pos -= 9

        if pos <= 180:
            num = 10 + (pos - 1) // 2
            d = (pos - 1) % 2
            if d == 0:
                print(num // 10)
            else:
                print(num % 10)
        else:
            pos -= 180
            num = 100 + (pos - 1) // 3
            d = (pos - 1) % 3
            if d == 0:
                print(num // 100)
            elif d == 1:
                print((num // 10) % 10)
            else:
                print(num % 10)