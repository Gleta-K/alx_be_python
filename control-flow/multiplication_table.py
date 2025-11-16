number = input("Enter a number to see its multiplication table:" )
X = int(number)
Y = range(1, 11)
for Y in range(1,11):
    Z = int(X * Y)
    print(f"{X} * {Y} = {Z}")