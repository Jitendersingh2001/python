def is_palindrome_str(number):
    number = str(number)
    return number == number[::-1]

def is_palindrome_without_str(number):
    original_number = number
    reversed_number = 0
    while original_number > 0:
        reminder = original_number % 10
        reversed_number = reversed_number * 10 + reminder
        original_number = original_number // 10
    return number == reversed_number

x = int(input("Enter the number: "))
print("Check with string type 1")
print("Check without string type 2")
y = input("Enter your choice: ")
if y == "1":
    res = is_palindrome_str(x)
elif y == "2":
    res = is_palindrome_without_str(x)
else:
    print("Choice is invalid !!")
    res = None

if res is not None:
    if res:
        print(f"{x} is a Palindrome number")
    else:
        print(f"{x} is not a Palindrome number")
