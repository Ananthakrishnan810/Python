#Python program to copy odd lines of one file to other
f1=open('D:\just\demo.txt','r')
f2=open('D:\just\print.txt','w')
str=f1.readlines()
for i in range(0,len(str)):
    if(i % 2!=0):
        f2.write(str[i])
f2=open('D:\just\print.txt','r')
str1=f2.read()
print(str1)
f1.close()
f2.close()


