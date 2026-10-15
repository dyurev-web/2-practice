n = int(input())

if 11 <= (n % 100) <= 14:
    print(n, "попугаев")
elif (n % 10) == 1:
    print(n, "попугай")
elif (n % 10) == 2 or (n % 10) == 3 or (n % 10) == 4:
    print(n, "попугая")
else:
    print(n, "попугаев")