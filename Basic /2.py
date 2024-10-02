x = input("Enter the first name: ")
y = input("Enter the second name: ")

x_age = int(input(f"Enter the age of {x}: "))
y_age = int(input(f"Enter the age of {y}: "))

print(f"{x} is {x_age} years old")
print(f"{y} is {y_age} years old")

if x_age > y_age:
    print(f"{x} is older than {y}")
elif x_age < y_age:
    print(f"{y} is older than {x}")
else:
    print(f"{x} and {y} are the same age")
