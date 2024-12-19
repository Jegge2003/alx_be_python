number = int(input("Enter a number to see its multiplication table: "))
product = 0
for num in range(1, 11):
    product = number * num
    print(f"{number} * {num} = {product}")
