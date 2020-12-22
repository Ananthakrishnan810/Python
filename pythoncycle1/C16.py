#program to find LCM of two numbers
def compute_lcm(x,y):
    if x>y:
        greater=x
    else:
        greater=y
    while(True):
        if((greater%x==0)and(greater%y==0)):
            lcm=greater
            break
        greater+=1
    return lcm
print("Enter the frist number:")
n1=int(input())
print("Enter the second number:")
n2=int(input())
print("The L.C.M is",compute_lcm(n1,n2))
