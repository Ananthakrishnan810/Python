#Find the biggest among 3 numbers
print("Enter the frist number:")
a=int(input())
print("Enter the second number:")
b=int(input())
print("Enter the third number:")
c=int(input())
if a>b:
    if a>c:
        print("The biggest number is:",a)
    else:
        print("The biggest number is:",c)
elif b>c:
    print("The biggest number is:",b)
else:
    print("The biggest number is:",c)
