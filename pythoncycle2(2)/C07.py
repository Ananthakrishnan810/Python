#List of color names entered by user and display first and last color
c=[]
x=int(input("Enter limit: "))
for i in range(1,x+1):
  a=input()
  c.append(a)
print(c)
print(c[0],c[-1])
