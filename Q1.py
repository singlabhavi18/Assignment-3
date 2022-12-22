while True:
    str = input("Enter the string: ")
    char = input("Enter the character you want to find: ")
    count = str.count(char)
    print("The number of occurrences of", char, "is", count)
    choice = input("Do you want to continue? [Y/N]: ")
    if choice.upper() == "N":
        break