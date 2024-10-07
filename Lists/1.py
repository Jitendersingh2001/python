#List is a collection which is ordered and changeable. Allows duplicate members.
#When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
#If you add new items to a list, the new items will be placed at the end of the list.
#create a list
#we use list constructor to create a list datatype
name_list =  list(("ram", "sham", "geeta"))
print(name_list)
name_list1 = ["Ram", "Sham", ["1",["1","2"]], "COME"]
print(name_list1)

#check the type of datatype name_list1
print(type(name_list1))
print(type(name_list))

#length of the list
print(len(name_list))
print(len(name_list1))

#access the first element of the list
print(name_list[0])
#access the last element of the list
print(name_list[-1])
print(name_list1[-2][-1][0])
print(name_list1[:2])

if "ram" in name_list:
    print("present")
else:
    print("absent")

#append to add the element in the last of the list
name_list.append("shiv")
print(name_list)
#insert to add the element at the specify index in the list
name_list.insert(1,"sidhi")
print(name_list)

#appned list in to list
name_list.extend(name_list1)
print(name_list)

#delete the specify element from the list
name_list.remove("ram")
print(name_list)

#pop used to remove the element from the specify index in the list
name_list.pop(2)
print(name_list)

#del used to remove the element from the specify index in the list
#and also used to delete the entire list
del name_list[2]
print(name_list)
del name_list #this will delete the entire list