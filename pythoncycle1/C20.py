#Program to check whether the given number is palindrome or not
print("Enter the number:")
a=int(input())
temp=a
rev=0
while a > 0:
    d=a%10
    rev=rev*10+d
    a//=10
if temp==rev:
    print("The given number is Palindrome")
else:
    print("The given number is not palindrome")
