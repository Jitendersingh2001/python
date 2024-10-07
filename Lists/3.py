# Define the count_element function to count occurrences of each element
def count_element(lst):
    element_count = {}
    for item in lst:
        if item in element_count:
            element_count[item] += 1
        else:
            element_count[item] = 1
    print("Element counts:", element_count)

# Get the number of elements from the user
x = int(input("How many elements do you want in the list? "))
list1 = []

# Input elements into the list
for i in range(x):
    element = input(f"Enter element {i+1} for the list: ")
    try:
        list1.append(int(element))
    except ValueError:
        list1.append(element)

print("The final list is:", list1)

# If list contains only integer elements, perform the count function
if all(isinstance(el, int) for el in list1):
    count_element(list1)
else:
    print("The list contains elements that are not numbers.")
