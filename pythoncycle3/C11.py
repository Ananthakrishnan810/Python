#Write a lamda functions find the area of a square,rectangle and triangle
#square:
print("Enter the width:")
a=int(input())
x=lambda b: b*b
print("The area is:")
print(x(a))

#rectangle:
print("Enter the length:")
a=int(input())
print("Enter the width:")
b=int(input())
x=lambda a,b: a*b
print("The area is:")
print(x(a,b))

#triangle:
print("Enter the length:")
a=int(input())
print("Enter the width:")
b=int(input())
x=lambda a,b: 0.5*a*b
print("The area is:")
print(x(a,b))

