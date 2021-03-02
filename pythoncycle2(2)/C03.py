#Prompt the user for a list of integers for all values >100,store 'over' instead
x=[]
n=int(input("Enter the limit :"))
for i in range(1,n+1):
  a=int(input("Enter the integer :"))
  if (a>100):
    x.append('over')
  else:
    x.append(a)
print("Modified list :" ,x)
