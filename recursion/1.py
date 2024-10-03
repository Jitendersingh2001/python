#Factorial of a number using recursion
def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return fact(n-1) * n
x = int(input("enter the number: "))
print(f"Factorial of a {x} = {fact(x)}")