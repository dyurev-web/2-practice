kir, ar, ser = map(int, input().split())
mx = kir
if ar > kir:
    mx = ar
if ser > mx:
    mx = ser
print(mx)