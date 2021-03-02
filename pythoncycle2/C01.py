#Generate positive list of numbers from a given list of inetgers
list=[10,-4,20,-30,50,70]
pnum=[num for num in list if num >=0]
print("positive numbers are:", *pnum)

#Square of N number
print("Enter the n :")
n=int(input())
def sq(n):
    l=[i*i for i in range(1,n+1)]
    return l
print (sq(n))

#Form a list of vowels selected from a given word
word=['apple']
l=[w[0] for w in word if w[0] in 'aeiou']
e=[w[4] for w in word if w[4] in 'aeiou']
print(l)
print(e)

#List ordinal value of each element of a word 
word=['apple']
print([ord(w[0]) for w in word ])
print([ord(w[1]) for w in word ])
print([ord(w[2]) for w in word ])
print([ord(w[3]) for w in word ])
print([ord(w[4]) for w in word ])
