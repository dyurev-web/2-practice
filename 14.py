n = int(input())

gall = n // (17 * 29)
ost = n % (17 * 29)
sikl = ost // 29
kn = ost % 29

if gall > 0:
    print(gall, "галлеонов")
if sikl > 0:
    print(sikl, "сикльей")
if kn > 0:
    print(kn, "кнатов")