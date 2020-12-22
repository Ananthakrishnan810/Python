#Program to generate multiplication table 
print("Enter the range:")
a=int(input())
print("Enter the number in which multiplication table print:")
b=int(input())
for x in range(1,a+1):
    print(b,'x',x,'=',b*x)
