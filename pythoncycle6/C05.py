#Write a Python program to write a Python dictionary to a csv file. After writing the CSV file
#read the CSV file and display the content.

f=open('D:\just\jj.txt','a')
import json
thisdict={"brand":"ford","company":"Mustang"}
result=json.dumps(thisdict)
f.write(result)
f.close()
f=open('D:\just\jj.txt','r')
print(f.read())