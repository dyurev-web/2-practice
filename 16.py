pswrd = input()
if len(pswrd) == 4:
    if not (1900 <= int(pswrd) <= 2050):
        if (pswrd[0] != pswrd[1] and pswrd[0] != pswrd[2] and
            pswrd[0] != pswrd[3] and pswrd[1] != pswrd[2] and
            pswrd[1] != pswrd[3] and pswrd[2] != pswrd[3]):
            print("OK")
        else:
            print("ERROR")
    else:
        print("ERROR")
else:
    print("ERROR")