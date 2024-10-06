#tower of hanoi using recursion in python
def tower_of_hanoi(disk, source, destination, helper):
    if disk == 1:
        print(f"disk 1 is moved from {source} to {destination}")
        return

    tower_of_hanoi(disk-1, source, destination, helper)
    print(f"Disk {disk} is moved from {source} to {destination}")
    tower_of_hanoi(disk-1, helper, destination,source)


n = int(input("enter the number of disks: "))
tower_of_hanoi(n, 'A', 'C',"B")