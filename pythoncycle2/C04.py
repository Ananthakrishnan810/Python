#Enter two list
#whether list are of the same length.
l1=[10,20,30,35]
l2=[5,15,25,35]
s1=len(l1)
s2=len(l2)
if s1==s2:
    print("The length of the two string are same")
else:
    print("The length of the two string are not same") 

#whether list sums to the same value
x1=sum(l1)
print("The sum of l1:",x1)
x2=sum(l2)
print("The sum of l2:",x2)
if x1==x2:
    print("The sum of the values are same")
else:
    print("The sum of the values are not same")

#whether any value occur in both.   
a=set(l1)
b=set(l2)
if(a&b):
    print(a&b)
else:
    print("No element is common")
