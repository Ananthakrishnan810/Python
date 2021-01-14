#Sort dictionary in ascending and desending order
dic={"one":1,
     "three":3,
     "two":2
     }
sort_order=sorted(dic.items(),key=lambda x:x[1])
for i in sort_order:
    print("The ascending order is",i[0],i[1])
print("\n")
sort_order1=sorted(dic.items(),key=lambda x:x[1],reverse=True)
for i in sort_order1:
    print("The descending order is",i[0],i[1])

