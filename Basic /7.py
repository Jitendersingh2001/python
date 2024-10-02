def count_string_char(name):
    count = 0
    for i in name:
        count += 1
    return count
def count_string_char_without_space(name):
    count = 0
    name = name.replace(" ","")
    for i in name:
        count += 1
    return count
x = input("enter the string: ")
print(f"char in a string is {count_string_char(x)}")
print(f"char in a string without space is {count_string_char_without_space(x)}")