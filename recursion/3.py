#sum of digit using recursion
def sum_of_digit(n):
    # Base case: if n is 0, return 0
    if n == 0:
        return 0
    else:
        # Recursive case: return last digit + sum of digits of the rest
        return n % 10 + sum_of_digit(n // 10)

# Input from the user
x = int(input("Enter the number for sum: "))
result = sum_of_digit(x)
print("The sum of the digits is:", result)
