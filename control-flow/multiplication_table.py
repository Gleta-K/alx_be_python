number = input("Enter a number to see its multipication table" )
X = int(number)
Y = range(1, 11)
for Y in Y:
    Z = int(X * Y)
    print(X, "*", Y, "=", Z)