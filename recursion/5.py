#Power of a number using recursion
def pow_number(n,p):
    if p == 0:
        return 1
    else:
        return n * pow_number(n,p-1)
x = int(input("enter the number: "))
y = int(input("enter the power for the number: "))
print(f"power of a number is : {pow_number(x,y)}")
