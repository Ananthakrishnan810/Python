#Write a Python program to read specific columns of a given CSV file and print the content of the columns.

import csv
f=open('D:\just\jj.csv','r')
reader=csv.reader(f)
for column in reader:
    print(column)
f.close()