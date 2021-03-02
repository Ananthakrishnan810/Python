#Find gcd of 2 numbers
def compute_gcf(x,y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1,smaller+1):
        if((x%i==0)and(y%i==0)):
            gcf=i;
    return gcf
print("Enter frist number:")
a=int(input())
print("Enter second number:")
b=int(input())
print("The G.C.F is:",compute_gcf(a,b))
        
