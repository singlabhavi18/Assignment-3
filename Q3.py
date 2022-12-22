lst = []
sqrd_lst = []
while True:
    x = int(input("Enter the number: "))
    lst.append(x)
    y = input("Do you want to continue? [Y/N]: ")
    if y.upper() == "N":
        break
for i in lst:
    z = (i, i**2)
    sqrd_lst.append(z)
print(sqrd_lst)