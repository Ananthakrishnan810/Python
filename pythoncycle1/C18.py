#program to reverse a number
print("Enter the number:")
a=int(input())
reverse=0
while a>0:
    reminder=a%10
    reverse=(reverse*10)+reminder
    a//=10
print("The reverse of a number is:",reverse)
