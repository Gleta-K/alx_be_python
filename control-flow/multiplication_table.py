number = int(input("Enter a number to see its multiplication table:" ))
Y = range(1, 11)
for Y in range(1,11):
    product = int(number * Y)
    print(f"{number} * {Y} = {product}")