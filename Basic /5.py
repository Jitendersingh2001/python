def factorial(number):
    result = 1
    while number > 0:
        result *= number
        number -= 1
    return result

x = int(input("Enter the number: "))
print(f"Factorial of a number is {factorial(x)}")
