str = "ABCDEFGHIJK"
len = len(str)
i = 0
while True:
    print(" " * i, str[0:len])
    len -= 2
    i += 1
    if len < 1:
        break