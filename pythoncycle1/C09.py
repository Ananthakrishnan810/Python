#Program to find largest among three numbers
print("Enter the first number:")
a=int(input())
print("Enter the second numer:")
b=int(input())
print("Enter the third number:")
c=int(input())
if a>b:
    if a>c:
        print("The largest is:", a)
    else:
        print("The largest is:", c)
if b>c:
    print("The largest is:", b)
else:
    print("The largest is:",c)
    
    
