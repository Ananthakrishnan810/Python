#program find the power of a number
def power(base,exp):
        if exp == 1:
             return(base)
        if exp!=1:
             return(base*power(base,exp-1))

print("Enter the base value:")
base=int(input())
print("Enter the expression value:")
exp=int(input())
print("The power",power(base,exp))
     
