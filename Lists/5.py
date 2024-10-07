#Write a function that returns the common elements between two lists.
def take_list(n:int) -> list:
    new_list = []

    for i in range(n):
        element = input(f"Enter element {i + 1} for the list: ")
        try:
            new_list.append(int(element))
        except ValueError:
            new_list.append(element)
    return new_list

def intersection_list(list_x,list_y):
    intersection_new_list = []
    for item in list_x:
        if item in list_y and item not in intersection_new_list:
            intersection_new_list.append(item)
    return intersection_new_list

x = int(input("How many elements do you want in the list 1? "))
list1 = take_list(x)
y = int(input("How many elements do you want in the list 2? "))
list2 = take_list(y)
print(f"list 1 is {list1}")
print(f"list 2 is {list2}")
list3 = intersection_list(list1, list2)
print(f"common elements between two lists are {list3}")