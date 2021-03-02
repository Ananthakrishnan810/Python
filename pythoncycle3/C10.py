#Generate all factors of a number.
print("Enter the number:")
a=int(input())
i=1
while i<=a:
    if a%i==0:
        print(i)
    i=i+1
