#Program to check the given character is even or odd
print("Enter the Character:")
a=str(input())
b=ord(a)
if b==97 or b==101 or b==105 or b==111 or b==117 or b==65 or b==69 or b==73 or b==79 or b==85:
    print("Character is Vovel")
else:
    print("Character is Consonant")
