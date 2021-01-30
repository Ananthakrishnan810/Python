#Print out all colors from color-list1 not contained in color-list2.
c1=[]
x=int(input("Enter limit for list1 :"))
for i in range(1,x+1):
  a=input()
  c1.append(a)
  p=set(c1)
print(p)
c2=[]
y=int(input("Enter limit for list2 : "))
for i in range(1,y+1):
  b=input()
  c2.append(b)
  q=set(c2)
print(q)
print(p.difference(q))
