#Accept a list of word and return the length of the longest word.
a=['hello','morning','come']
print(a)
length1=len(a[0])
length2=len(a[1])
length3=len(a[2])
if length1>length2:
    if length1>length3:
        print("The length of longest word",length1)
    else:
        print("The length of longest word",length3)
elif length2>length1:
    if length2>length3:
        print("The length of longest word",length2)
    else:
        print("The length of longest word",length3)
        
