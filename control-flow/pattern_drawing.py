size = int(input("Enter the size of the pattern:" ))
row = 0
while row < size:
    for i in range(0, size):
        print("*", end = "")
    print("\n")
    row = row + 1
