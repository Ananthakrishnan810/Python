class time:
    def __init__(self,h,m,s):
        self.__h=h
        self.__m=m
        self.__s=s

    def __add__(self, other):
        a1=self.__h + other.__h
        a2=self.__m + other.__m
        a3=self.__s + other.__s
        print("The sum of the hour",a1)
        print("The sum of the minutes",a2)
        print("The sum of the second",a3)

a=int(input("Enter the hour:"))
b=int(input("Enter the minute:"))
c=int(input("Enter the second:"))
t1=time(a,b,c)
d=int(input("Enter the hour:"))
e=int(input("Enter the minute:"))
f=int(input("Enter the second:"))
t2=time(d,e,f)
print(t1+t2)
