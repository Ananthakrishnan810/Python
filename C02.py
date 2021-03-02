#program to display fibonacci series
print("Enter the number of terms:")
t=int(input())
n1=0
n2=1
count=0
if t<=0:
    print("please enter a positive integer")
elif t==1:
    print("fibonacci sequence upto",t)
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < t:
        print(n1)
        n=n1+n2
        n1=n2
        n2=n
        count+=1
