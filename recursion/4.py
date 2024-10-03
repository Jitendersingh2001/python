#Reverse a string using a recursion
def reverse_string(s):
    # Base case: if the string is empty or has one character
    if len(s) <= 1:
        return s
    # Recursive case: return the last character + reverse of the rest of the string
    #s[:-1] used to omit the last char from string
    return s[-1] + reverse_string(s[:-1])

x = input("enter the name: ")
print(f"name is {x}")
y = reverse_string(x)
print(f"reversed name is {y}")
