def remove_duplicates(lst):
    unique_list = []

    for item in lst:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list

# Input elements into the list
x = int(input("How many elements do you want in the list? "))
list1 = []

for i in range(x):
    element = input(f"Enter element {i + 1} for the list: ")
    try:
        list1.append(int(element))
    except ValueError:
        list1.append(element)

# Remove duplicates
list1 = remove_duplicates(list1)
print("The final list after removing duplicates is:", list1)
