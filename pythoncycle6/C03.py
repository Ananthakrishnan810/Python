#Write a Python program to read each row from a given csv file and print a list of strings.
f=open('D:\just\jj.csv','r')
str=f.readlines()
list1=list(str)
print(list1)
f.close()