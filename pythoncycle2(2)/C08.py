#Accept an integer n and compute n+nn+nnn
a=int(input("Enter the integer : "))
n1=int("%s" %a)
n2=int("%s%s" %(a,a))
n3=int("%s%s%s" %(a,a,a))
print("value of n+nn+nnn is : ",n1+n2+n3)
