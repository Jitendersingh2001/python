#without converting into string
def is_armstrong(number):
    original_number = number
    power = len(str(number))
    result = 0

    while number > 0:
        last_digit = number % 10
        result += last_digit ** power
        number = number //10

    return result == original_number

x = int(input("Enter the number for check: "))
res = is_armstrong(x)
if res:
    print(f"{x} is armstrong number")
else:
    print(f"{x} number is not armstrong")



