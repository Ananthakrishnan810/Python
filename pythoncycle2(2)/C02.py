#Leap years from current year to a final year entered by the user
s=int(input("Enter starting year: "))
e=int(input("Enter ending year: "))
print("Leap years between",s,"and",e)
while (s<=e):
    if ((s%400==0) or ((s%4==0) and (s%100!=0))):
      print(s)
    s=s+1
