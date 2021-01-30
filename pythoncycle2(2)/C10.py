#Single string separated with space from two strings by swapping the character at position 1.
x=input("Enter the first string : ")
y=input("Enter the second string : ")
def swapch(x,y): 
  a = y[:1] + x[1:]
  b = x[:1] + y[1:]
  return a + ' ' + b
print(swapch(x,y))
