def print_table(number):
    for i in range(1,11):
        result = number * i
        print(f"{number} * {i} = {result}")

x = int(input("enter the table number "))
print_table(x)