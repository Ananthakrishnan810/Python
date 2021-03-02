#Count the occurence of each word in a line of text.
def wordoccur(n,p):
    x=n.split(" ")
    c=0
    for i in range(0,len(x)):
        if(p==x[i]):
            c=c+1
    return c
print("Enter the string:")
n=str(input())
print("Enter the word to count the occurence:")
p=str(input())
print("The occurence of the",p,"is",wordoccur(n,p))
