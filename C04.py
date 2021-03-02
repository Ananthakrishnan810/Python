#Generate a list of four digit numbers in a given range with all their digits even and the number is a perfect square.

a=int(input("Enter the lower digit:"))
b=int(input("Enter the upper digit:"))
import random
print(random.randint(a,b))
c=[]
c=[x for x in range(a,b)if(int(x**0.5)**2==x and int(x%2==0))]
print(c)

