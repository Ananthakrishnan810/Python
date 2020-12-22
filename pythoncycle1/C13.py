#Program to find the factorial of a number
print("Enter the range:")
a=int(input())
fact=1
for x in range(1,a+1):
    fact=fact*x
print("The factorial",fact)
